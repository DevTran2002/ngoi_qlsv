# -*- coding: utf-8 -*-
# from odoo import http


# class Qlnv(http.Controller):
#     @http.route('/qlnv/qlnv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qlnv/qlnv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qlnv.listing', {
#             'root': '/qlnv/qlnv',
#             'objects': http.request.env['qlnv.qlnv'].search([]),
#         })

#     @http.route('/qlnv/qlnv/objects/<model("qlnv.qlnv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qlnv.object', {
#             'object': obj
#         })
