# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EgyGrowersPurchaseRequest(models.Model):
    _inherit = 'sprogroup.purchase.request.line'

    qty_on_hand = fields.Float(string='Qty on Hand')

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            name = self.product_id.name
            if self.product_id.code:
                name = '[%s] %s' % (name, self.product_id.code)
            if self.product_id.description_purchase:
                name += '\n' + self.product_id.description_purchase
            self.product_uom_id = self.product_id.uom_id.id
            self.product_qty = 1
            self.name = name
            product = self.env['product.product'].search([('id','=',self.product_id.id)])
            self.qty_on_hand = product.qty_available