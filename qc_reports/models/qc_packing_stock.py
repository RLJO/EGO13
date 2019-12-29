from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class QC_PACKING_STOCK(models.Model):
    _name = 'qc.packing.stock'
    _rec_name = 'id'
    production_order=fields.Many2one('mrp.production')
    production_ids = fields.One2many(comodel_name='qc.packing.stock.line', inverse_name='production_id')


    @api.depends('production_ids')
    def get_report_production_data(self):
        production_record = self.env['mrp.production'].search([])


        sale_order_list = []
        for record in self:

            record.production_ids.unlink()
            for item in production_record:
                print(item.create_date)
                print(item.name)
                create_date = datetime.strftime(item.create_date, '%Y-%m-%d')
                print(create_date)
                for line in item.production_ids:
                    self.production_ids.create({
                        'production_id':record.id,
                        'description': line.description,
                        'customer_name': line.customer_name.id,
                        'manufacturing_name':item.name,
                        'create_date':create_date,

                    })


class QC_PACKING_STOCK_line(models.Model):
        _name = 'qc.packing.stock.line'
        production_id = fields.Many2one(comodel_name='qc.packing.stock')

        customer_name = fields.Many2one('res.partner', string="Partner Name")
        description = fields.Char(string="Description")
        manufacturing_name = fields.Char()
        create_date = fields.Date()







