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
import requests


class WizardDailyBook(models.TransientModel):
    _name = 'marcos.ipf.daily.wizard'

    branches_id = fields.Many2one('marcos.ipf.book.branches', string="Sucursal", required=True)
    date = fields.Date("Fecha", required=True)

    @api.one
    def generate(self):
        #'/daily_book/:serial/:day/:month/:year'
        date = self.date.split("-")
        day = date[2]
        month = date[1]
        year = date[0]
        for lines in self.branches_id.line_ids:
            if lines.printer_id.available:

                host = "%s/daily_book/%s/%s/%s/%s" % (lines.printer_id.host, lines.printer_id.name, day, month, year)
                try:
                    response = requests.get(host)
                    if response.status_code == 200:
                        filename = response.headers['Content-Disposition'].split('filename=')[1].replace('"','')
                        new_book_id = self.env["marcos.ipf.book.daily"].create({"branches_id": self.branches_id.id, "printer_id": lines.printer_id.id, "date": self.date, "book_name": filename})
                        self.env["marcos.ipf.book.daily"].save_book(new_book_id ,response.text)
                except Exception as e:
                    print e


class WizardMonthlyBook(models.TransientModel):
    _name = 'marcos.ipf.monthly.wizard'

    period = fields.Char(u"Período", size=6)

    @api.one
    def generate(self):
        #'/daily_book/:serial/:day/:month/:year'
        month = self.period[:2]
        year = self.period[2:]


        host = "http://192.168.0.14:4567/monthly_book/%s/%s" % (month, year)
        try:
            response = requests.get(host)
            if response.status_code == 200:
                filename = response.headers['Content-Disposition'].split('filename=')[1].replace('"', '')
                new_book_id = self.env["marcos.ipf.book.monthly"].create({"period": self.period})
                self.env["marcos.ipf.book.monthly"].save_book(new_book_id, response.text)
        except Exception as e:
            print e