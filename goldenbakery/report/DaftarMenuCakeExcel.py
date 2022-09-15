from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.goldenbakery.report_menucake_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, menucake):
        sheet = workbook.add_worksheet('Daftar Menu Cake')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama')
        sheet.write(2, 1, 'Harga Modal')
        sheet.write(2, 2, 'Harga Jual')
        sheet.write(2, 3, 'Stock')
        sheet.write(2, 4, 'Category')
        row = 3
        col = 0
        for obj in menucake: 
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.harga_modal)
            sheet.write(row, col+2, obj.harga_jual)
            sheet.write(row, col+3, obj.stok)
            for xxx in obj.categorycake_id:
                sheet.write(row, col+4, xxx.name)
                col += 1
            row += 1