# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _, exceptions
# import datetime

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class MANUFACTURINGReportsWizard(models.Model):
    _name = 'manufacturing.report.wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)



    def get_manufacturing_report(self):

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,

            },

        }
        return self.env.ref('manufacturing.report_manufacturing_details').report_action(self, data=data)


class manufacturingREPORT(models.AbstractModel):
    _name = 'report.manufacturing.print_manufacturing_details_template'
    _description = 'manufacturing Report'


    def _get_report_values(self, docids, data=None):

            date_from = data['form']['date_from']
            date_to = data['form']['date_to']



            docs = []

            manufacturing_record = self.env['mrp.production'].search(
                [('create_date', '>=', date_from), ('create_date', '<=', date_to),('state','=','done')])


            for item in manufacturing_record:
                create_date = datetime.strftime(item.create_date, '%Y-%m-%d')
                total_cost = 0
                for rec in item.move_raw_ids:
                    product_cost = rec.product_id.standard_price * rec.product_uom_qty

                    total_cost += product_cost

                docs.append({
                    'manufacturing_id': item.name,
                    'track_no': item.track_no,
                    'create_date': create_date,
                    'total_cost': total_cost,

                })
            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_to': date_to,
                'date_from': date_from,
                'docs': docs,
            }







