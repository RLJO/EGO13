# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class EgyGrowersAccountPayment(models.Model):
    _inherit = ['account.payment', 'mail.thread']
    _inherit = 'account.payment',


    beneficiary_name = fields.Char(string='Beneficiary name')
    beneficiary_account_no = fields.Char(string='Beneficiary account no')
    transer_date = fields.Date(string='Transfer Date')
    state = fields.Selection([('draft', 'Draft'),('md_approval', 'MD Approval'),('ceo_approval','CEO Approval'),('pending','Pending'), ('posted', 'Posted'), ('sent', 'Sent'), ('reconciled', 'Reconciled'), ('cancelled', 'Cancelled')],
                             readonly=True, default='draft', copy=False, string="Status", track_visibility=True)
    invoice_ref = fields.Many2one(comodel_name='account.move',string='Invoice Number')


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        super(EgyGrowersAccountPayment, self)._onchange_partner_id()
        self.invoice_ref = ''
        vendor_bills = self.env['account.move'].search([('state', '=', 'open'),
                                                           ('type', '=', 'in_invoice'),
                                                           ('partner_id','=',self.partner_id.id)])
        customer_invoices = self.env['account.move'].search([('state', '=', 'open'),
                                                                ('type', '=', 'out_invoice'),
                                                                ('partner_id','=',self.partner_id.id)])
        res = {}
        if self.payment_type == 'outbound':
            res['domain'] = {'invoice_ref': [('id', 'in', vendor_bills.ids)]}
        elif self.payment_type == 'inbound':
            res['domain'] = {'invoice_ref': [('id', 'in', customer_invoices.ids)]}

        return res

    def action_account_payment_md_confirm(self):
        for order in self:
            order.state = 'md_approval'
        return True

    def action_ceo_confirm(self):
        for order in self:
            order.state = 'ceo_approval'
        return True

    def action_pending_confirm(self):
        for order in self:
            order.state = 'pending'
        return True

    def action_outbound_post(self):
        """ Create the journal items for the payment and update the payment's state to 'posted'.
            A journal entry is created containing an item in the source liquidity account (selected journal's default_debit or default_credit)
            and another in the destination reconcilable account (see _compute_destination_account_id).
            If invoice_ids is not empty, there will be one reconcilable move line per invoice to reconcile with.
            If the payment is a transfer, a second journal entry is created in the destination journal to receive money from the transfer account.
        """
        for rec in self:

            if rec.state != 'pending':
                raise UserError(_("Only a Pending payment can be posted."))

            if any(inv.state != 'open' for inv in rec.invoice_ids):
                raise ValidationError(_("The payment cannot be processed because the invoice is not open!"))

            # keep the name in case of a payment reset to draft
            if not rec.name:
                # Use the right sequence to set the name
                if rec.payment_type == 'transfer':
                    sequence_code = 'account.payment.transfer'
                else:
                    if rec.partner_type == 'customer':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.customer.invoice'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.customer.refund'
                    if rec.partner_type == 'supplier':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.supplier.refund'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.supplier.invoice'
                rec.name = self.env['ir.sequence'].with_context(ir_sequence_date=rec.payment_date).next_by_code(sequence_code)
                if not rec.name and rec.payment_type != 'transfer':
                    raise UserError(_("You have to define a sequence for %s in your company.") % (sequence_code,))

            # Create the journal entry
            amount = rec.amount * (rec.payment_type in ('outbound', 'transfer') and 1 or -1)
            move = rec._create_payment_entry(amount)

            # In case of a transfer, the first journal entry created debited the source liquidity account and credited
            # the transfer account. Now we debit the transfer account and credit the destination liquidity account.
            if rec.payment_type == 'transfer':
                transfer_credit_aml = move.line_ids.filtered(lambda r: r.account_id == rec.company_id.transfer_account_id)
                transfer_debit_aml = rec._create_transfer_entry(amount)
                (transfer_credit_aml + transfer_debit_aml).reconcile()
            print (">>>>>>>>>>>>>>>>>>>>>",rec, move ,)
            rec.write({'state': 'posted', 'move_name': move.name})
        return True
