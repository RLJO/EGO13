from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError

class MPRPRODUCTIONCUSTOM(models.Model):
    _inherit = 'mrp.production'
    _rec_name = 'track_no'

    track_no = fields.Char(compute="get_tracking_no",store=True)
    @api.depends('origin')
    def get_tracking_no(self):
        for item in self:
            sale_order=self.env['sale.order'].search([('name','=',self.origin)])

            for rec in sale_order:
                if rec.name:

                    item.track_no=rec.tracking_number




class MRPBOMCUSTOM(models.Model):
    _inherit = 'mrp.bom'
    analytic_account=fields.Many2one('account.analytic.account')
