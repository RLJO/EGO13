# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.tools import email_re, email_split, email_escape_char, float_is_zero, float_compare, \
    pycompat, date_utils

class EgyGrowersAccountMove(models.Model):
    _inherit = 'account.move'

    invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice Lines', oldname='invoice_line',
        readonly=True, states={'draft': [('readonly', False)],'proforma': [('readonly', False)]}, copy=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order',compute='_get_sale_order',store=True)
    tracking_number = fields.Char(related='sale_order_id.tracking_number',inverse='sale_order_inverse', store=True)
    state = fields.Selection([
	('draft', 'Draft'),
            ('posted', 'Posted'),
            ('cancel', 'Cancelled'),
        ('proforma', 'Pro-Forma'),
    ], string='Status', index=True, readonly=True, default='draft',
        track_visibility='onchange', copy=False,)
    shipping_term = fields.Char(related='sale_order_id.shipping_term', inverse='sale_order_inverse', string='Shipping Term')
    etd = fields.Char(related='sale_order_id.etd', inverse='sale_order_inverse', string='ETD')
    eta = fields.Char(related='sale_order_id.eta', inverse='sale_order_inverse', string='ETA')
    proforma_date = fields.Date(string="Proforma Date",
                                readonly=True, states={'proforma': [('readonly', False)]}, index=True,
                                help="generated on change state from draft to preforma")

    @api.depends('invoice_line_ids')
    def _get_sale_order(self):
        for rec in self:
            sales = rec.invoice_line_ids.mapped('sale_line_ids').mapped('order_id')
            if sales:
                order_id = self.env['sale.order'].search([('id', '=', sales.ids[0])])
                rec.sale_order_id = order_id
            else:
                rec.sale_order_id = False

    def sale_order_inverse(self):
        if self.sale_order_id:
            self.sale_order_id.tracking_number = self.tracking_number
            self.sale_order_id.shipping_term = self.shipping_term
            self.sale_order_id.etd = self.etd
            self.sale_order_id.eta = self.eta


    def proforma(self):
        for rec in self:
            rec.state = 'proforma'
            rec.proforma_date = fields.Date.today()

    def action_invoice_open(self):
        # lots of duplicate calls to action_invoice_open, so we remove those already open
        to_open_invoices = self.filtered(lambda inv: inv.state != 'open')
        if to_open_invoices.filtered(lambda inv: not inv.partner_id):
            raise UserError(_("The field Vendor is required, please complete it to validate the Vendor Bill."))
        if to_open_invoices.filtered(lambda inv: inv.state != 'proforma') and self.type == 'out_invoice':
            raise UserError(_("Invoice must be in proforma state in order to validate it."))
        if to_open_invoices.filtered(
                lambda inv: float_compare(inv.amount_total, 0.0, precision_rounding=inv.currency_id.rounding) == -1):
            raise UserError(_(
                "You cannot validate an invoice with a negative total amount. You should create a credit note instead."))
        if to_open_invoices.filtered(lambda inv: not inv.account_id):
            raise UserError(
                _('No account was found to create the invoice, be sure you have installed a chart of account.'))
        to_open_invoices.action_date_assign()
        to_open_invoices.action_move_create()
        return to_open_invoices.invoice_validate()




    def _get_sale_order_tracking_number(self):
        for rec in self:
            sales = rec.invoice_line_ids.mapped('sale_line_ids').mapped('order_id')
            if sales:
                order_id = self.env['sale.order'].search([('id','=',sales.ids[0])])
                rec.tracking_number = order_id.tracking_number
