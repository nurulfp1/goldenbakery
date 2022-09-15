from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.goldenbakery.report_categorycake_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, categorycake):
        sheet = workbook.add_worksheet('Daftar Category Cake')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Category')
        sheet.write(2, 1, 'Kode Category')
        sheet.write(2, 2, 'Kode Chiller')
        sheet.write(2, 3, 'Jumlah Item')
        sheet.write(2, 4, 'Daftar Isi')
        row = 3
        col = 0
        for obj in categorycake: 
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.kode_categ)
            sheet.write(row, col+2, obj.kode_chiller)
            sheet.write(row, col+3, obj.jml_item)
            sheet.write(row, col+4, obj.daftar)
            # for item in obj.menucake_ids:
            #     sheet.write(row, col+5, item.name)
            #     col += 1
            row += 1