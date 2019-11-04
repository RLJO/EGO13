# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EgyGrowersSaleOrder(models.Model):
    _inherit = 'sale.order'

    tracking_number = fields.Char(string='Tracking No')
    shipping_term = fields.Char(string='Shipping Term')
    etd = fields.Char(string='ETD')
    eta = fields.Char(string='ETA')

