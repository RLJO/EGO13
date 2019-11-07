# -*- coding: utf-8 -*-
from odoo import http

# class PartnerEnhancement(http.Controller):
#     @http.route('/partner_enhancement/partner_enhancement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_enhancement/partner_enhancement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_enhancement.listing', {
#             'root': '/partner_enhancement/partner_enhancement',
#             'objects': http.request.env['partner_enhancement.partner_enhancement'].search([]),
#         })

#     @http.route('/partner_enhancement/partner_enhancement/objects/<model("partner_enhancement.partner_enhancement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_enhancement.object', {
#             'object': obj
#         })