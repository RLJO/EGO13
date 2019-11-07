# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields,api,_, exceptions
from urllib.parse import urljoin
from odoo.addons.website.models.website import slugify
from odoo.exceptions import UserError
import xlwt
import base64
from datetime import datetime


class EgyGrowersLogisticsReport(models.TransientModel):
    _name = 'logistics.report.wiz'
    _description = 'Logistics Report'


    start_date = fields.Date('Start Date',)
    end_date = fields.Date('End Date',)


    def open_xl_report(self):
        stock_picking_obj = self.env['stock.picking']
        domain = []
        date_from = ''
        date_to = ''
        invoice_ref = ''
        domain.append(('type_of_operation_code', '=', 'outgoing'))
        self.ensure_one()
        if self.start_date and self.end_date:
            date_from = self.start_date
            date_to = self.end_date
            domain.append(('scheduled_date', '>=', date_from))
            domain.append(('scheduled_date', '<=', date_to))

        pickings = stock_picking_obj.search(domain, order="scheduled_date desc")

        style1 = xlwt.easyxf('font:height 200;align: horiz center,vert center;font:bold True;'
                             'pattern: pattern solid,  fore_colour gray50;borders: right medium,'
                             'right_colour black,left medium,left_colour black,top medium,'
                             'top_colour black,bottom medium,bottom_colour black;')
        style0 = xlwt.easyxf(
            'font:height 180;align: horiz center,vert center;font:bold False;pattern: pattern solid,  fore_colour gray25;borders: right medium,right_colour black,left medium,left_colour black,top medium,top_colour black,bottom medium,bottom_colour black;')

        workbook = xlwt.Workbook()

        sheet = workbook.add_sheet('Logistics Report')
        sheet.write_merge(0, 0, 1, 4, 'Logistic Report', style1)
        sheet.write(1, 1, 'Date From:', style1)
        sheet.write(1, 2, str(date_from), style1)
        sheet.write(1, 3, 'Date To:', style1)
        sheet.write(1, 4, str(date_to), style1)

        sheet.write(3, 1, 'Name', style1)
        sheet.write(3, 2, 'Actual Loading Day', style1)
        sheet.write(3, 3, 'ETA', style1)
        sheet.write(3, 4, 'ETD', style1)
        sheet.write(3, 5, 'Partner', style1)
        sheet.write(3, 6, 'POL', style1)
        sheet.write(3, 7, 'POD', style1)
        sheet.write(3, 8, 'Invoice', style1)
        sheet.write(3, 9, 'Tracking Number', style1)
        sheet.write(3, 10, 'Product', style1)
        sheet.write(3, 11, 'Shipping Line', style1)
        sheet.write(3, 12, 'Door to door', style1)
        sheet.write(3, 13, 'No of Cntr', style1)
        sheet.write(3, 14, 'Booking Number', style1)
        sheet.write(3, 15, 'Vessel', style1)
        sheet.write(3, 16, 'Container Number', style1)
        sheet.write(3, 17, 'PL Number', style1)
        sheet.write(3, 18, 'Data Logger', style1)
        sheet.write(3, 19, 'Packhouse', style1)
        sheet.write(3, 20, 'Shipping Notice', style1)
        sheet.write(3, 21, 'Documents', style1)
        sheet.write(3, 22, 'Doc Tracking No', style1)

        n = 4  ## row
        i = 1  ## column
        column = 1
        ## adjust sheet column's width
        for column in range(1, 23):
            if column == 10:
                sheet.col(column).width = 10000
            else:
                sheet.col(column).width = 6000
        for picking in pickings:
            for move in picking.move_lines:
                sale_id = move.picking_id.sale_id.id
                if sale_id:
                    invoice_ref = self.env['account.invoice'].search([('sale_order_id', '=', sale_id)],limit=1).number

                sheet.write(n, i , move.picking_id.name, style0)
                sheet.write(n, i + 1 , str(move.picking_id.actual_loading_day), style0)
                sheet.write(n, i + 2 , str(move.picking_id.vessel_eta), style0)
                sheet.write(n, i + 3 , str(move.picking_id.vessel_etd), style0)
                sheet.write(n, i + 4 , move.picking_id.partner_id.name, style0)
                sheet.write(n, i + 5 , move.picking_id.pol_id.name, style0)
                sheet.write(n, i + 6 , move.picking_id.pod_id.name, style0)
                sheet.write(n, i + 7 , invoice_ref, style0)
                sheet.write(n, i + 8 , move.picking_id.tracking_number, style0)
                sheet.write(n, i + 9 , move.product_id.name, style0)
                sheet.write(n, i + 10 , move.picking_id.shipping_line_id.name, style0)
                sheet.write(n, i + 11 , move.picking_id.door_to_door.name, style0)
                sheet.write(n, i + 12 , move.picking_id.no_of_cntr, style0)
                sheet.write(n, i + 13 , move.picking_id.booking_number, style0)
                sheet.write(n, i + 14 , move.picking_id.vessel_id.name, style0)
                sheet.write(n, i + 15 , move.picking_id.container_number, style0)
                sheet.write(n, i + 16 , move.picking_id.pl_number, style0)
                sheet.write(n, i + 17 , move.picking_id.data_logger, style0)
                sheet.write(n, i + 18 , move.picking_id.packhouse_id.name, style0)
                sheet.write(n, i + 19 , str(move.picking_id.shipping_notice), style0)
                sheet.write(n, i + 20 , str(move.picking_id.documents), style0)
                sheet.write(n, i + 21 , move.picking_id.doc_tracking_no, style0)

                n += 1

        ams_time = datetime.now()
        date = ams_time.strftime('%m-%d-%Y %H.%M.%S')
        filename = ('/tmp/Report' + '-' + date + '.xls')
        workbook.save(filename)

        fp = open(filename, "rb")
        file_data = fp.read()
        attach_id = self.env['report.wizard'].create({'attachment': base64.encodestring(file_data),
                                                      'attach_name': 'Report.xls'})
        fp.close()
        if len(pickings) > 0:
            return {
                'type': 'ir.actions.act_window',
                'name': ('Report'),
                'res_model': 'report.wizard',
                'res_id': attach_id.id,
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
            }
        else:
            raise exceptions.ValidationError(
                _("There are no pickings .."))


class PaymentWizard(models.TransientModel):
    _name = 'report.wizard'
    _description = 'Report Details'

    attachment = fields.Binary('Excel Report File', nodrop=True, readonly=True)
    attach_name = fields.Char('Attachment Name')

