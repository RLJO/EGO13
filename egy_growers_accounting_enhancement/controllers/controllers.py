# -*- coding: utf-8 -*-
from odoo import http

# class AccountingEnhancement(http.Controller):
#     @http.route('/accounting_enhancement/accounting_enhancement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accounting_enhancement/accounting_enhancement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('accounting_enhancement.listing', {
#             'root': '/accounting_enhancement/accounting_enhancement',
#             'objects': http.request.env['accounting_enhancement.accounting_enhancement'].search([]),
#         })

#     @http.route('/accounting_enhancement/accounting_enhancement/objects/<model("accounting_enhancement.accounting_enhancement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accounting_enhancement.object', {
#             'object': obj
#         })