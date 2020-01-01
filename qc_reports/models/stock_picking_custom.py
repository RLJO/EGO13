from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class STOCKPICKING(models.Model):
    _inherit = 'stock.picking'
    qc_ids = fields.One2many(comodel_name='stock.picking.line',inverse_name='qc_line')



class STOCKPICKINGline(models.Model):
    _name = 'stock.picking.line'
    qc_line = fields.Many2one('stock.picking')
    description=fields.Char(string="Description")
    date = fields.Date(string="Date")







