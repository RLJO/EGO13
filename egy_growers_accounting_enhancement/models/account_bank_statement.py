# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang, format_date


class EgyGrowersAccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    statment_type = fields.Selection(selection=[('money_in','Money In'),('money_out','Money Out')],default='money_in',string='Type')
    expense_type = fields.Selection(selection=[('documented','Documented'),
                                               ('undocumented','Undocumented')],string='Expense Type')
    date = fields.Date(required=True, states={'confirm': [('readonly', True)]}, index=True, copy=False, )


    @api.depends('line_ids', 'balance_start', 'line_ids.amount', 'balance_end_real')
    def _end_balance(self):
        if self.statment_type == 'money_in':
            self.total_entry_encoding = sum([line.amount for line in self.line_ids])
            self.balance_end = self.balance_start + self.total_entry_encoding
            self.difference = self.balance_end_real - self.balance_end
            self.balance_end_real = self.balance_end
        else:
            self.total_entry_encoding = sum([line.amount for line in self.line_ids])
            if self.total_entry_encoding >= 0:
                self.balance_end = self.balance_start - self.total_entry_encoding
            else:
                self.balance_end = self.balance_start + self.total_entry_encoding
                self.balance_end_real = self.balance_end
                self.difference = self.balance_end_real - self.balance_end

    @api.model
    def create(self, vals):
        print('daate ',vals.get('date'))
        total_entry_encoding = 0.0
        if vals.get('statment_type'):
            for rec in vals.get('line_ids'):
                total_entry_encoding += rec[2].get('amount')
            if vals.get('statment_type') == 'money_out':
                if total_entry_encoding >= 0 :
                    vals['balance_end'] = vals['balance_start'] - total_entry_encoding
                else:
                    vals['balance_end'] = vals['balance_start'] + total_entry_encoding
            else:
                if total_entry_encoding >= 0 :
                    vals['balance_end'] = vals['balance_start'] + total_entry_encoding
                else:
                    vals['balance_end'] = vals['balance_start'] - total_entry_encoding
            vals['balance_end_real'] = vals['balance_end']
            vals['difference'] = vals['balance_end_real'] - vals['balance_end']
        print('daate222 ',vals.get('date'))

        line = super(EgyGrowersAccountBankStatement, self).create(vals)
        print('line daate ',line.date)

        if line.statment_type == 'money_out':
            for record in line.line_ids:
                if record.amount > 0:
                    record.amount = - record.amount

        return line

    def write(self, vals):
        total_entry_encoding = 0.0
        if vals.get('statment_type'):
            for rec in vals.get('line_ids'):
                total_entry_encoding += rec[2].get('amount')

            if vals.get('statment_type') == 'money_out':
                if total_entry_encoding >= 0:
                    vals['balance_end'] = vals['balance_start'] - total_entry_encoding
                else:
                    vals['balance_end'] = vals['balance_start'] + total_entry_encoding
            else:
                if total_entry_encoding >= 0:
                    vals['balance_end'] = vals['balance_start'] + total_entry_encoding
                else:
                    vals['balance_end'] = vals['balance_start'] - total_entry_encoding
            vals['balance_end_real'] = vals['balance_end']
            vals['difference'] = vals['balance_end_real'] - vals['balance_end']
        # print('vals',vals)
        line = super(EgyGrowersAccountBankStatement, self).write(vals)
        if self.statment_type == 'money_out':
            for record in self.line_ids:
                if record.amount > 0:
                    record.amount = - record.amount

        return line

