from odoo import api, fields, models


class RawIngridient(models.Model):
    _name = 'goldenbakery.rawingridient'
    _description = 'New Description'

    name = fields.Char(string='Nama Bahan')
    unit = fields.Selection([
        ('kg', 'Kg'), 
        ('kwintal', 'Kwintal'), 
        ('ton', 'ton'),
        ('liter', 'Liter'),
        ('butir', 'Butir'),
        ('pcs', 'Pcs')
    ], string='Unit')
    harga_beli = fields.Integer(string='Harga',required=True)
    supplier_id = fields.Many2many(comodel_name='goldenbakery.supplier', 
                                   string='Supplier')

    stok = fields.Integer(string='Stok')


class Supplier(models.Model):
    _name = 'goldenbakery.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    rawingridient_id = fields.Many2many(comodel_name='goldenbakery.rawingridient', 
                                 string='Bahan Baku')

