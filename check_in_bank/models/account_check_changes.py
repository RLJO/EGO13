from odoo import fields, models, _, api
from datetime import date
from odoo.exceptions import except_orm, Warning, RedirectWarning

##################
## Ahmed Salama ##
##################

class account_check_operation_changes(models.Model):
    _inherit = 'account.check.operation'
    operation = fields.Selection([
        # from payments
        ('holding', 'Receive'),
        ('deposited', 'Deposit'),
        ('selled', 'Sell'),
        ('delivered', 'Deliver'),
        # usado para hacer transferencias internas, es lo mismo que delivered
        # (endosado) pero no queremos confundir con terminos, a la larga lo
        # volvemos a poner en holding
        ('transfered', 'Transfer'),
        ('handed', 'Hand'),
        ('withdrawed', 'Withdrawal'),
        # from checks
        ('reclaimed', 'Claim'),
        ('rejected', 'Rejection'),
        ('debited', 'Debit'),
        ('inbank', 'Inbank'),
        ('returned', 'Return'),
        ('changed', 'Change'),
        ('cancel', 'Cancel'),
    ],
        required=True,
    )
class account_check_changes(models.Model):
    _inherit = 'account.check'
    ## add inbank account field
                
                
    inbank_account_id = fields.Many2one('account.account', string='In Bank Account')
    partner_id = fields.Many2one(comodel_name='res.partner',string="Check Partner")
    ## Add state inbank
    state = fields.Selection([
        ('draft', 'Draft'),
        ('holding', 'Holding'),
        ('deposited', 'Deposited'),
        ('selled', 'Selled'),
        ('delivered', 'Delivered'),
        ('transfered', 'Transfered'),
        ('reclaimed', 'Reclaimed'),
        ('withdrawed', 'Withdrawed'),
        ('handed', 'Handed'),
        ('inbank', 'Inbank'),
        ('debited', 'Debited'),
        ('returned', 'Returned'),
        ('changed', 'Changed'),
        ('rejected', 'Rejected'),
        ('cancel', 'Cancel'),
    ],
        required=True,
        default='draft',
        copy=False,
        compute='_compute_state',
        store=True,
    )



    def open_wizard_inbank_check(self):
        """
        open wizard to chose account of debit
        :return:
        """
        action = self.env.ref('check_in_bank.action_wizard_inbank')
        result = action.read()[0]
        res = self.env.ref('check_in_bank.check_action_inbank_form_view', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['target'] = 'new'
        inbank_account = self.company_id._get_check_account('inbank')
        result['context'] = {'default_action_type':'inbank','default_account_id':inbank_account and inbank_account.id or False}
        return result
    
    def bank_debit_action(self):
        """
        open wizard to choose journal for debit account
        :return:
        """
        self.ensure_one()
        action = self.env.ref('check_in_bank.action_wizard_inbank')
        result = action.read()[0]
        res = self.env.ref('check_in_bank.check_action_inbank_form_view', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['target'] = 'new'
        result['context'] = {'default_action_type':'bank_debit',
                             'default_inbank_account_id':self.inbank_account_id.id if self.inbank_account_id else False}
        return result

    def bank_return_action(self):
        """
		open wizard to choose journal for debit account
		:return:
		"""
        self.ensure_one()
        action = self.env.ref('check_in_bank.action_wizard_inbank')
        result = action.read()[0]
        res = self.env.ref('check_in_bank.check_action_inbank_form_view', False)
        result['views'] = [(res and res.id or False, 'form')]
        holding_account = self.company_id._get_check_account('holding')
        result['target'] = 'new'
        result['context'] = {'default_action_type': 'returned',
                             'default_inbank_account_id': self.inbank_account_id.id if self.inbank_account_id else False,
                             'default_partner_id': self.partner_id and self.partner_id.id or False,
                             'default_account_id': holding_account and holding_account.id or False}
        return result
    
    def change_state_handed(self):
        """
        on start show button to hand check
        :return:
        """
        if self.state == 'holding'and self.operation_ids:
            for line in self.operation_ids:
                line.write({'operation':'handed'})
       
