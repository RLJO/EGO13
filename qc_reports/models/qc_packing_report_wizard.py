# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _, exceptions
# import datetime

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class QCPACKINGREPORTWIZARD(models.Model):
    _name = 'qc.packing.wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)



    def get_qc_packing_report(self):

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,

            },

        }
        return self.env.ref('qc_reports.report_qc_packing').report_action(self, data=data)


class QCPACKINGREPORT(models.AbstractModel):
    _name = 'report.qc_reports.print_qc_packing_details_template'
    _description = 'QC Packing Report'


    def _get_report_values(self, docids, data=None):

            date_from = data['form']['date_from']
            date_to = data['form']['date_to']



            docs = []

            manufacturing_record = self.env['mrp.production'].search(
                [('create_date', '>=', date_from), ('create_date', '<=', date_to),('state','=','done')])


            for item in manufacturing_record:
                create_date = datetime.strftime(item.create_date, '%Y-%m-%d')
                print(create_date)
                for line in item.production_ids:
                    docs.append({
                        'description': line.description,
                        'customer_name': line.customer_name.name,
                        'manufacturing_name': item.name,
                        'create_date': create_date,

                    })

            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_to': date_to,
                'date_from': date_from,
                'docs': docs,
            }







