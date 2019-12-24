from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class PURCHASEORDER(models.Model):
    _inherit = 'purchase.order'
    approve_check=fields.Boolean()
    partner_id = fields.Many2one('res.partner', string='Vendor',
                                 change_default=True, tracking=True,required=False,
                                 domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
                                 help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
    company_id = fields.Many2one('res.company', 'Company', required=False,index=True, default=lambda self: self.env.company.id)



    # state = fields.Selection(
    #                              [('draft', 'RFQ'), ('sent', 'RFQ Sent'), ('approve1', 'First-Approve') , ('approve2', 'Manager-Approve'), ('purchase', 'Purchase Order'), ('done', 'Locked'), ('cancel', 'Cancelled')])
    def approve_purchase(self):
        self.state='approve1'
        self.approve_check=True
    def approve_manager(self):
        self.state='approve2'

    def button_confirm(self):
        if self.approve_check == True:
            self.approve_check = False
            for order in self:
                if order.state not in ['draft', 'sent','approve1','approve2']:
                    continue
                order._add_supplier_to_product()
                # Deal with double validation process
                if order.company_id.po_double_validation == 'one_step' \
                        or (order.company_id.po_double_validation == 'two_step' \
                            and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id,
                            order.date_order or fields.Date.today())) \
                        or order.user_has_groups('purchase.group_purchase_manager'):
                    order.button_approve()
                # else:
                #     order.write({'state': 'approve2'})
            return True
        else:
            raise UserError(
                _('Sorry you Can not Confirm Quotation To purchase Order YOU Must Take first and Second Manager Approve '))

