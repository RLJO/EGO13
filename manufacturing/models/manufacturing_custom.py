from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class MPRPRODUCTIONCUSTOM(models.Model):
    _inherit = 'mrp.production'
    _rec_name = 'track_no'

    track_no = fields.Char(store=True)
    # @api.depends('origin')
    # def get_tracking_no(self):
    #     for item in self:
    #         sale_order=self.env['sale.order'].search([('name','=',self.origin)])
    #
    #         for rec in sale_order:
    #             if rec.name:
    #
    #                 item.track_no=rec.tracking_number
    #



class MRPBOMCUSTOM(models.Model):
    _inherit = 'mrp.bom'
    analytic_account=fields.Many2one('account.analytic.account')

class SALESORDER(models.Model):
        _inherit = 'sale.order'


        def _action_confirm(self):
            print('ibrahimmmmm')
            """ Implementation of additionnal mecanism of Sales Order confirmation.
                This method should be extended when the confirmation should generated
                other documents. In this method, the SO are in 'sale' state (not yet 'done').
            """

            # create an analytic account if at least an expense product
            for order in self:
                if any([expense_policy not in [False, 'no'] for expense_policy in order.order_line.mapped('product_id.expense_policy')]):
                    if not order.analytic_account_id:
                        order._create_analytic_account()
            mo=self.env['mrp.production'].search([('origin','=',self.name)])
            for i in mo:

                i.track_no=self.tracking_number

            return True


