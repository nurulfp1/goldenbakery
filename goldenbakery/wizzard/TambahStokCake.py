from odoo import api, fields, models


class TambahStokCake(models.Model):
    _name = 'goldenbakery.tambahstokcake'

    menucake_id = fields.Many2one(
        comodel_name='goldenbakery.menucake', 
        string='Nama',
        required=True)
    
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    
    def button_tambah_stok_cake(self):
        for rec in self:
            self.env['goldenbakery.menucake'].search([('id', '=', rec.menucake_id.id)]).write({'stok' : rec.menucake_id.stok + rec.jumlah})