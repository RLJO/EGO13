from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class MPRPRODUCTION(models.Model):
    _inherit = 'mrp.production'
    production_ids=fields.One2many(comodel_name='mrp.production.line',inverse_name='production_line')



class MPRPRODUCTIONCUSTOM_line(models.Model):
    _name = 'mrp.production.line'
    production_line = fields.Many2one('mrp.production')
    customer_name=fields.Many2one('res.partner', string="Partner Name")
    description=fields.Char(string="Description")






