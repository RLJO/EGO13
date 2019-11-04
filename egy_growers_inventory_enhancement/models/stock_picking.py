# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EgyGrowersStockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def _get_sale_order(self):
        for rec in self:
            if rec.sale_id:
                rec.sale_order_id = rec.sale_id

    sale_order_id = fields.Many2one(comodel_name='sale.order',compute=_get_sale_order)
    tracking_number = fields.Char(related='sale_order_id.tracking_number',inverse='tracking_number_inverse',string='Tracking No', store=True)
    actual_loading_day = fields.Date(string='Actual Loading Day')
    vessel_etd = fields.Date(string='Vessel ETD')
    vessel_eta = fields.Date(string='Vessel ETA')
    shipping_line_id = fields.Many2one(comodel_name='shipping.line',string='Shipping Line')
    pol_id = fields.Many2one(comodel_name='pol',string='POL')
    pod_id = fields.Many2one(comodel_name='pod',string='POD')
    door_to_door = fields.Many2one(comodel_name='door.to.door',string='Door to door')
    no_of_cntr = fields.Char(string='No. of Cntr')
    booking_number = fields.Char(string='Booking Number')
    vessel_id = fields.Many2one(comodel_name='vessel',string='Vessel name')
    container_number = fields.Char(string='Container Number')
    pl_number = fields.Char(string='B/L No')
    data_logger = fields.Char(string='Data Logger')
    packhouse_id = fields.Many2one(comodel_name='packhouse',string='Packhouse')
    shipping_notice = fields.Date(string='Shipping Notice')
    documents = fields.Date(string='Documents')
    doc_tracking_no = fields.Char(string='Doc Tracking No.')
    type_of_operation_code = fields.Selection(related='picking_type_id.code', store=True)

    @api.multi
    def tracking_number_inverse(self):
        if self.sale_order_id:
            self.sale_order_id.tracking_number = self.tracking_number


class EgyGrowersShippingLine(models.Model):
    _name = 'shipping.line'
    _rec_name = 'name'
    _order = 'name'
    _description = 'shipping line'

    name = fields.Char()


class EgyGrowersPOL(models.Model):
    _name = 'pol'
    _rec_name = 'name'
    _order = 'name'
    _description = 'name'

    name = fields.Char()

class EgyGrowersPOD(models.Model):
    _name = 'pod'
    _rec_name = 'name'
    _order = 'name'
    _description = 'name'

    name = fields.Char()

class EgyGrowersDoorTODoor(models.Model):
    _name = 'door.to.door'
    _rec_name = 'name'
    _order = 'name'
    _description = 'name'

    name = fields.Char()

class EgyGrowersVessel(models.Model):
    _name = 'vessel'
    _rec_name = 'name'
    _order = 'name'
    _description = 'name'

    name = fields.Char()

class EgyGrowersBackhouse(models.Model):
    _name = 'packhouse'
    _rec_name = 'name'
    _order = 'name'
    _description = 'name'

    name = fields.Char()



