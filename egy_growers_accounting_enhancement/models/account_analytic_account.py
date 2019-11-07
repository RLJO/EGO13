# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class EgyGrowersAccountInvoice(models.Model):
    _inherit = 'account.analytic.account'

    # _sql_constraints = [
    #     ('unique_analytic_account_name',
    #      'unique(name)', 'Analytic account name should be unique!')]

    @api.constrains('name')
    def _check_unique_analytic_account(self):
        if not self.name:
            return True
        elif len(self.search([('name','=',self.name)])) >1:
            raise ValueError('Analytic Account name must be unique!')