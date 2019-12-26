from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class INTERNALLOGISTIC(models.Model):
    _name = 'internal.logistic'
    _rec_name = 'stock_pick_id'
    stock_pick_id = fields.Many2one('stock.picking')
    source_document = fields.Char(related='stock_pick_id.origin',store=True,readonly=1)
    location_dest_id = fields.Many2one(related='stock_pick_id.location_dest_id',store=True,readonly=1)
    type_of_car = fields.Many2one(related='stock_pick_id.type_of_car',store=True,readonly=1)
    supplier_id = fields.Many2one(related='stock_pick_id.supplier_id',store=True,readonly=1)
    date = fields.Datetime(related='stock_pick_id.scheduled_date',store=True,readonly=1)



