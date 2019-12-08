# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _, exceptions
# import datetime

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class LogisticReportsWizard(models.Model):
    _name = 'logistic.report.wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    supplier = fields.Many2one('transport.supplier')


    def get_logistic_report(self):

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
                'supplier':self.supplier.id,
            },

        }
        return self.env.ref('logistic.report_logistic_details').report_action(self, data=data)


class LOGISTICREPORT(models.AbstractModel):
    _name = 'report.logistic.print_logistic_details_template'
    _description = 'Logistic Report'


    def _get_report_values(self, docids, data=None):

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        supplier= data['form']['supplier']


        docs = []
       
        if supplier:
            logistic_record = self.env['internal.logistic'].search(
                [('create_date', '>=', date_from), ('create_date', '<=', date_to), ('supplier_id', '=', supplier)])
            print(logistic_record)
            for item in logistic_record:
                create_date = datetime.strftime(item.create_date, '%Y-%m-%d')
                docs.append({
                    'stock_pick_id':item.stock_pick_id.name,
                    'source_document':item.source_document,
                    'location_dest_id':item.location_dest_id.name,
                    'type_of_car':item.type_of_car.name,
                    'supplier_id':item.supplier_id.name,
                    'create_date':create_date,

                             })
            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_to': date_to,
                'date_from': date_from,
                'docs': docs,
            }




        else:  
            logistic_record = self.env['internal.logistic'].search(
                [('create_date', '>=', date_from), ('create_date', '<=', date_to)])
            print('else',logistic_record)
            for item in logistic_record:
                create_date = datetime.strftime(item.create_date, '%Y-%m-%d')
                docs.append({'stock_pick_id': item.stock_pick_id.name,
                             'source_document': item.source_document,
                             'location_dest_id': item.location_dest_id.name,
                             'type_of_car': item.type_of_car.name,
                             'supplier_id': item.supplier_id.name,
                             'create_date': create_date,

                             })
            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_to': date_to,
                'date_from': date_from,
                'docs': docs,
            }



