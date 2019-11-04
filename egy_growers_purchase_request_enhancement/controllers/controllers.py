# -*- coding: utf-8 -*-
from odoo import http

# class EgyGrowersPurchaseRequestEnhancement(http.Controller):
#     @http.route('/egy_growers_purchase_request_enhancement/egy_growers_purchase_request_enhancement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/egy_growers_purchase_request_enhancement/egy_growers_purchase_request_enhancement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('egy_growers_purchase_request_enhancement.listing', {
#             'root': '/egy_growers_purchase_request_enhancement/egy_growers_purchase_request_enhancement',
#             'objects': http.request.env['egy_growers_purchase_request_enhancement.egy_growers_purchase_request_enhancement'].search([]),
#         })

#     @http.route('/egy_growers_purchase_request_enhancement/egy_growers_purchase_request_enhancement/objects/<model("egy_growers_purchase_request_enhancement.egy_growers_purchase_request_enhancement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('egy_growers_purchase_request_enhancement.object', {
#             'object': obj
#         })