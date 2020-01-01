# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _, exceptions
# import datetime

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class QCPACKHOUSEREPORTWIZARD(models.Model):
    _name = 'qc.packhouse.wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    partner_id = fields.Many2one('res.partner')



    def get_qc_packhouse_report(self):

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
                'partner_id':self.partner_id.id,

            },

        }
        return self.env.ref('qc_reports.report_qc_packhouse').report_action(self, data=data)


class QCPACKHOUSEREPORT(models.AbstractModel):
    _name = 'report.qc_reports.print_qc_packhouse_details_template'
    _description = 'QC packhouse Report'


    def _get_report_values(self, docids, data=None):

            date_from = data['form']['date_from']
            date_to = data['form']['date_to']
            partner_id = data['form']['partner_id']



            docs = []
            if partner_id:

                picking_record = self.env['stock.picking'].search([('create_date', '>=', date_from), ('create_date', '<=', date_to),('partner_id','=',partner_id)])
                print(picking_record)


                for item in picking_record:

                    for line in item.qc_ids:
                        docs.append({
                            'picking_order': item.name,
                            'partner_id': item.partner_id.name,
                            'description': line.description,
                            'date': line.date,


                        })
            else:
                picking_record = self.env['stock.picking'].search([('create_date', '>=', date_from), ('create_date', '<=', date_to)])

                for item in picking_record:

                    for line in item.qc_ids:
                        docs.append({
                            'picking_order':item.name,
                             'partner_id': item.partner_id.name,
                            'description': line.description,
                            'date': line.date,

                        })

            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_to': date_to,
                'date_from': date_from,
                'docs': docs,
            }







