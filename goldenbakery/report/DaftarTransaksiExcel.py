from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.goldenbakery.report_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, transaksi):
        sheet = workbook.add_worksheet('Daftar Transaksi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'No. Nota')
        sheet.write(2, 1, 'Nama Pembeli')
        sheet.write(2, 2, 'Tgl. Transaksi')
        sheet.write(2, 3, 'Total Pembayaran')
        sheet.write(2, 4, 'Detail Produk')
        row = 3
        col = 0
        for obj in transaksi: 
            col = 0
            date_style = workbook.add_format({'text_wrap': True, 'num_format': 'mm-dd-yyyy'})
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, obj.tgl_transaksi, date_style)
            sheet.write(row, col+3, obj.total_bayar)
            for item in obj.detailtransaksi_ids:
                sheet.write(row, col+4, item.menucake_id.name)
                col += 1
            row += 1