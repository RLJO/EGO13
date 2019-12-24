from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class SALESORDER(models.Model):
    _inherit = 'sale.order'
    approve_check = fields.Boolean()



    state = fields.Selection([('draft', 'Quotation'), ('sent', 'Quotation Sent'), ('approve1', 'Sales-Approve'), ('approve2', 'Manager-Approve'), ('sale', 'Sale Order'), ('done', 'Locked'), ('cancel', 'Cancelled')])
    def approve_sale(self):
        self.state = 'approve1'
        self.approve_check=True
    def approve_manager(self):
        self.state = 'approve2'
    def action_cancel(self):

        self.approve_check = False

        return self.write({'state': 'cancel'})

    def action_confirm(self):

        if self.approve_check == True:
            self.approve_check = False

            if self._get_forbidden_state_confirm() & set(self.mapped('state')):
                raise UserError(_(
                    'It is not allowed to confirm an order in the following states: %s'
                ) % (', '.join(self._get_forbidden_state_confirm())))

            for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
                order.message_subscribe([order.partner_id.id])
            self.write({
                'state': 'sale',
                'date_order': fields.Datetime.now()
            })
            self._action_confirm()
            if self.env.user.has_group('sale.group_auto_done_setting'):
                self.action_done()
            return True
        else:
            raise UserError(_('Sorry you Can not Confirm Quotation To Sale Order YOU Must Take Sales Manager Approve First'))


class RESPARTNER(models.Model):
    _inherit = 'res.partner'
    location = fields.Text()
    contracts_count =fields.Integer(compute="_get_contarcts_value",readonly=1)
    mobile2 = fields.Char()
    mobile3 = fields.Char()
    def _get_contarcts_value(self):
        contract_id = self.env['contract'].search([('partner_id', '=', self.id)])
        count=0
        for rec in contract_id:
            count += 1
        self.contracts_count=count



    def open_contract_view(self):
        action = self.env.ref('ego_sale_purchase_custom.contract_action')
        contract_id = self.env['contract'].search([('partner_id', '=', self.id)])


        if contract_id:
            for item in contract_id:

                    result = action.read()[0]
                    result['views'] = [(self.env.ref('ego_sale_purchase_custom.contract_tree_view').id, 'tree'),(self.env.ref('ego_sale_purchase_custom.contract_form_view').id, 'form')]
                    result['domain'] = [('partner_id', '=', self.id)]

                    result.update({'view_type': 'form',
                                   'view_mode': 'form' 'tree',
                                   'target': 'current',
                                   'res_id': item.id,
                                   })

                    return result

        else:
            action = self.env.ref('ego_sale_purchase_custom.contract_action')
            result = action.read()[0]
            result['views'] = [(self.env.ref('ego_sale_purchase_custom.contract_form_view').id, 'form')]
            result['context'] = {'default_partner_id': self.id,
                                 'default_description': '', }
            result.update({'view_type': 'form',
                           'view_mode': 'form',
                           'target': 'current'})

            return result





