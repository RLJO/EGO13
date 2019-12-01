from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class PLANNINGFIRST(models.Model):
    _name = 'planning.first'
    _rec_name = 'name'
    name = fields.Char()


class PLANNINGSECOND(models.Model):
    _name = 'planning.second'
    _rec_name='name'
    name = fields.Char()

class PLANNINGTHIRD(models.Model):
    _name = 'planning.third'
    _rec_name='name'
    name = fields.Char()


