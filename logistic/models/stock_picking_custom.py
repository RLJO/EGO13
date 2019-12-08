from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class STOCKPICKINGCUSTOM(models.Model):
    _inherit = 'stock.picking'
    _rec_name = 'name'


    type_of_car = fields.Many2one('transport.type')
    supplier_id = fields.Many2one('transport.supplier')

class TRANSPORTSUPLLIER(models.Model):
    _name = 'transport.supplier'
    name = fields.Char()
    _rec_name = 'name'

class typeofcar(models.Model):
    _name = 'transport.type'
    name = fields.Char()
    _rec_name = 'name'