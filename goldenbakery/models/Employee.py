from odoo import api, fields, models


class Employee(models.Model):
    _name = 'goldenbakery.employee'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    jenis_kelamin = fields.Selection([
        ('laki', 'Laki-laki'),
        ('perempuan', 'Perempuan')
    ], string='Jenis Kelamin', default='laki')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')
    gaji = fields.Integer(string='Gaji')
    tunjangan = fields.Integer(string='Tunjangan')
    



class Chef(models.Model):
    _name = 'goldenbakery.chef'
    _inherit = 'goldenbakery.employee'
    _description = 'New Description'

    id_chef = fields.Char(string='ID Chef')

    _sql_constraints = [
        ('id_chef_unik', 'unique (id_chef)', 'ID Sudah ada !!!'),
    ]


class Cashier(models.Model):
    _name = 'goldenbakery.cashier'
    _inherit = 'goldenbakery.employee'
    _description = 'New Description'

    id_cashier = fields.Char(string='ID Cashier')

    _sql_constraints = [
        ('id_cashier_unik', 'unique (id_cashier)', 'ID Sudah ada !!!'),
    ]


class CleaningService(models.Model):
    _name = 'goldenbakery.cleaningservice'
    _inherit = 'goldenbakery.employee'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')

    _sql_constraints = [
        ('id_cln_unik', 'unique (id_cln)', 'ID Sudah ada !!!'),
    ]
    


    
    
