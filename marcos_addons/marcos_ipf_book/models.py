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

from openerp import models, fields, api
import base64


class IpfBranches(models.Model):
    _name = "marcos.ipf.book.branches"
    _inherit = 'mail.thread'

    name = fields.Char("Nombre", required=True, help=u"Aquí debe de colocar el nombre o referencia que describa una sucursal o área")
    line_ids = fields.One2many("marcos.ipf.book.branches.lines", "branches_id", string="Impresoras",
                               help=u"Lista de impresoras que pertenecen a esta sucursal, de esta forma el usuario responsable de la sucursal extraerá, diariamente el libro de diario de las impresoras asignadas a su área.")
    user_id = fields.Many2one("res.users", "Responsable", help=u"Usuario responsable de extraer el libro de diario para esta sucursal.", required=True)

    def action_confirm(self):
        print "ok"

class IpfBranchesLines(models.Model):
    _name = "marcos.ipf.book.branches.lines"

    branches_id = fields.Many2one("marcos.ipf.book.branches", u"Impresoras")
    printer_id = fields.Many2one("marcos.ipf.book.printer", "Impresora")


class IpfPrinter(models.Model):
    _name = "marcos.ipf.book.printer"
    _inherit = 'mail.thread'

    name = fields.Char(u"Nombre o referencia de la impresora", required=True, help=u"Nombre o referencia de la impresora instalada")
    host = fields.Char(u"Host de la impresora", required=True, help=u"Nombre del Host o la ip donde se encuentra la impresora conectada")
    available = fields.Boolean(u"Activa", help=u"Indica si la impresora esta activa para la extracción del libro")


class IpfBookDaily(models.Model):
    _name = "marcos.ipf.book.daily"
    _inherit = 'mail.thread'

    branches_id = fields.Many2one("marcos.ipf.book.branches", u"Sucursal")
    printer_id = fields.Many2one("marcos.ipf.book.printer", u"Impresora")
    book_name = fields.Char(u"Libro", readonly=True)
    book = fields.Binary(u"Libro diario")
    date = fields.Date(u"Fecha")

    def save_book(self, new_book_id, book):
        book = base64.b64encode(book)
        new_book_id.write({"book": book})
        return True


class IpfBookMonthly(models.Model):
    _name = "marcos.ipf.book.monthly"
    _inherit = 'mail.thread'

    book = fields.Binary(u"Libro mensual")
    period = fields.Char(u"Período", size=6)

    def save_book(self, new_book_id, book):
        book = base64.b64encode(book)
        book_name = fields.Char(u"Libro", readonly=True)
        new_book_id.write({"book": book})
        return True