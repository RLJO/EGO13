from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class QCHARVESTINSPECTION(models.Model):
    _name = 'qc.harvest.inspection'
    _rec_name = 'partner_id'
    partner_id=fields.Many2one('res.partner')
    date=fields.Date()
    name=fields.Char()









