from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class MPRPRODUCTION(models.Model):
    _inherit = 'res.partner'
    qc_ids=fields.One2many(comodel_name='res.partner.line',inverse_name='qc_line')



class MPRPRODUCTIONCUSTOM_line(models.Model):
    _name = 'res.partner.line'
    qc_line = fields.Many2one('res.partner')
    estimate_test=fields.Char(string="Estimate")
    date=fields.Date(string="Date")
    sample_attach = fields.Binary('Sample File',filename="attach_name")
    attach_name = fields.Char('Attachment file')
    mrl_attach = fields.Binary('MRL File', filename="mrl_name")
    mrl_name = fields.Char('Attachment MRL')






