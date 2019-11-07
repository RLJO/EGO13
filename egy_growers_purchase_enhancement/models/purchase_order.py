# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RequestforQuotation(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('ceo_approval', 'CEO Approval'),
        ('accounting_team_approval', 'Accounting Team Approval'),
        ('md_approval', 'MD Approval'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', track_visibility='onchange')
    current_state = fields.Char(compute='_get_current_state')

    def _get_current_state(self):
        for rec in self:
            rec.current_state = rec.state

    def action_ceo_confirm(self):
        for order in self:
            order.state = 'ceo_approval'
        return True

    def action_accounting_team_confirm(self):
        for order in self:
            order.state = 'accounting_team_approval'
        return True

    def action_md_confirm(self):
        for order in self:
            order.state = 'md_approval'
        return True

    def action_back_accounting_team_approval_state(self):
        for order in self:
            order.state = 'accounting_team_approval'
        return True

    def action_back_draft_state(self):
        for order in self:
            order.state = 'draft'
        return True

    def action_back_ceo_state(self):
        for order in self:
            order.state = 'ceo_approval'
        return True


    def button_confirm(self):
        for order in self:
            if order.state not in ['md_approval']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step' \
                    or (order.company_id.po_double_validation == 'two_step' \
                        and order.amount_total < self.env.user.company_id.currency_id._convert(
                        order.company_id.po_double_validation_amount, order.currency_id, order.company_id,
                        order.date_order or fields.Date.today())) \
                    or order.user_has_groups('purchase_enhancement.egy_growers_accounting_team'):
                    # or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True
