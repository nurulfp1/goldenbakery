from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.goldenbakery.report_cleaningservice_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, cleaningservice):
        sheet = workbook.add_worksheet('Daftar Employee cleaningservice')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'ID Cleaning Service')
        sheet.write(2, 1, 'Nama')
        sheet.write(2, 2, 'Alamat')
        sheet.write(2, 3, 'Jenis Kelamin')
        sheet.write(2, 4, 'Tgl. Lahir')
        sheet.write(2, 5, 'Gaji')
        sheet.write(2, 6, 'Tunjangan')
        row = 3
        col = 0
        for obj in cleaningservice: 
            col = 0
            date_style = workbook.add_format({'text_wrap': True, 'num_format': 'mm-dd-yyyy'})
            sheet.write(row, col, obj.id_cln)
            sheet.write(row, col+1, obj.name)
            sheet.write(row, col+2, obj.alamat)
            sheet.write(row, col+3, obj.jenis_kelamin)
            sheet.write(row, col+4, obj.tgl_lahir, date_style)
            sheet.write(row, col+5, obj.gaji)
            sheet.write(row, col+6, obj.tunjangan)
            row += 1