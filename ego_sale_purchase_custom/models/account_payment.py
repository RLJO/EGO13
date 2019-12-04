from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class ACCOUNTPAYMENT(models.Model):
    _inherit = 'account.payment'

    payment_actual_date=fields.Date()