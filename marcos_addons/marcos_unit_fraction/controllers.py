# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013-2015 Marcos Organizador de Negocios SRL http://marcos.do
#    Write by Eneldo Serrata (eneldo@marcos.do)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import http

# class MarcosUnitFraction(http.Controller):
#     @http.route('/marcos_unit_fraction/marcos_unit_fraction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marcos_unit_fraction/marcos_unit_fraction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('marcos_unit_fraction.listing', {
#             'root': '/marcos_unit_fraction/marcos_unit_fraction',
#             'objects': http.request.env['marcos_unit_fraction.marcos_unit_fraction'].search([]),
#         })

#     @http.route('/marcos_unit_fraction/marcos_unit_fraction/objects/<model("marcos_unit_fraction.marcos_unit_fraction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marcos_unit_fraction.object', {
#             'object': obj
#         })