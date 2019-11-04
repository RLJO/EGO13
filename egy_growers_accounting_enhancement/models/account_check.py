# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.tools import email_re, email_split, email_escape_char, float_is_zero, float_compare, \
    pycompat, date_utils

class EgyGrowersAccountCheck(models.Model):
    _inherit = 'account.check'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('holding', 'Holding'),
        ('deposited', 'Deposited'),
        ('selled', 'Selled'),
        ('delivered', 'Delivered'),
        ('transfered', 'Transfered'),
        ('reclaimed', 'Reclaimed'),
        ('withdrawed', 'Withdrawed'),
        ('handed', 'Handed'),
        ('inbank', 'Inbank'),
        ('debited', 'Debited'),
        ('returned', 'Returned'),
        ('changed', 'Changed'),
        ('rejected', 'Rejected'),
        ('cancel', 'Cancel'),
    ],
        required=True,
        default='draft',
        copy=False,
        compute='_compute_state',
        store=True,
        track_visibility=True,
    )
