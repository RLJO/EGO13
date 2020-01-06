# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _, exceptions
# import datetime

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class QCFARMREPORTWIZARD(models.Model):
    _name = 'qc.farm.wizard'

    date_from = fields.Date()
    date_to = fields.Date()
    partner_id = fields.Many2one('res.partner')



    def get_qc_farm_report(self):

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
                'partner_id':self.partner_id.id,

            },

        }
        return self.env.ref('qc_reports.report_qc_farm').report_action(self, data=data)


class QCFARMREPORT(models.AbstractModel):
    _name = 'report.qc_reports.print_qc_farm_details_template'
    _description = 'QC Farm Report'


    def _get_report_values(self, docids, data=None):

            date_from = data['form']['date_from']
            date_to = data['form']['date_to']
            partner_id = data['form']['partner_id']



            docs = []
            if partner_id:

                partner_record = self.env['res.partner'].search([('id','=',partner_id)])
                print(partner_record)


                for item in partner_record:

                    for line in item.qc_ids:
                        docs.append({
                            'partner_id': item.name,
                            'estimate_test': line.estimate_test,
                            'date': line.date,
                            'sample_attach': line.attach_name,
                            'mrl_attach':line.mrl_name,

                        })
            else:
                partner_record = self.env['res.partner'].search([])

                for item in partner_record:

                    for line in item.qc_ids:
                        docs.append({
                            'partner_id': item.name,
                            'estimate_test': line.estimate_test,
                            'date': line.date,
                            'sample_attach': line.sample_attach,
                            'mrl_attach': line.mrl_attach,

                        })

            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_to': date_to,
                'date_from': date_from,
                'docs': docs,
            }







