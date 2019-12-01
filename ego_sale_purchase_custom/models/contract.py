from odoo import fields,api,models,_

class EGOCONTRACT(models.Model):
    _name = 'contract'
    _rec_name='partner_id'


    partner_id = fields.Many2one('res.partner')
    description=fields.Char()

