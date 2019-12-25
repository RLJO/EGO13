from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class SALESORDER(models.Model):
    _inherit = 'sale.order'
    approve_check = fields.Boolean()
    deliver_to=fields.Many2one('res.partner')
    notify = fields.Many2one('res.partner')
    grow_w=fields.Char()
    net_w = fields.Char()
    no_containers = fields.Char()

    def _prepare_invoice(self):
        print('hello ibrahim')
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        journal = self.env['account.move'].with_context(force_company=self.company_id.id,
                                                        default_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (
            self.company_id.name, self.company_id.id))

        invoice_vals = {
            'ref': self.client_order_ref or '',
            'type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'invoice_payment_ref': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'deliver_to_inv':self.deliver_to,
            'notify_inv': self.notify,
            'grow_w_inv': self.grow_w,
            'net_w_inv': self.net_w,
            'no_containers_inv': self.no_containers,
        }
        return invoice_vals

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





