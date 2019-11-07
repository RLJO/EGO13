# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EgyGrowersLogisticsReport(models.Model):
    _name = 'report.egy_growers_inventory_enhancement.report_logistics'

    test = fields.Char()