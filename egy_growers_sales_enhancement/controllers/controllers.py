# -*- coding: utf-8 -*-
from odoo import http

# class SalesEnhancement(http.Controller):
#     @http.route('/sales_enhancement/sales_enhancement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_enhancement/sales_enhancement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_enhancement.listing', {
#             'root': '/sales_enhancement/sales_enhancement',
#             'objects': http.request.env['sales_enhancement.sales_enhancement'].search([]),
#         })

#     @http.route('/sales_enhancement/sales_enhancement/objects/<model("sales_enhancement.sales_enhancement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_enhancement.object', {
#             'object': obj
#         })