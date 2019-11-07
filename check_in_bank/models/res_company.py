# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import Warning

## Ahmed Salama Code Start ---->





class ResCompany(models.Model):
    _inherit = 'res.company'

    inbank_check_account_id = fields.Many2one(
        'account.account',
        'In Bank Check Account',
        help='In Bank Checks account for third checks, '
        'for eg. "In Bank Checks"',
        # domain=[('type', 'in', ['other'])],
    )

    def _get_check_account(self, type):
        """
        Add type in bank to get by default from company configs
        :param type:
        :return: INBANK/SUPER
        """
        self.ensure_one()
        if type == 'inbank':
            account = self.inbank_check_account_id
            return account
        return super(ResCompany, self)._get_check_account(type)

## Ahmed Salama Code End.
