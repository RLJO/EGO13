# -*- coding: utf-8 -*-
from odoo import http

# class InventoryEnhancement(http.Controller):
#     @http.route('/inventory_enhancement/inventory_enhancement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_enhancement/inventory_enhancement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_enhancement.listing', {
#             'root': '/inventory_enhancement/inventory_enhancement',
#             'objects': http.request.env['inventory_enhancement.inventory_enhancement'].search([]),
#         })

#     @http.route('/inventory_enhancement/inventory_enhancement/objects/<model("inventory_enhancement.inventory_enhancement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_enhancement.object', {
#             'object': obj
#         })