# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProductChanges(models.Model):
    _inherit = 'product.product'

    is_raw = fields.Boolean(string='Raw')