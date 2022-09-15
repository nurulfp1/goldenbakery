from odoo import api, fields, models


class MenuCake(models.Model):
    _name = 'goldenbakery.menucake'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    harga_modal = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    categorycake_id = fields.Many2one(comodel_name='goldenbakery.categorycake', 
                                        string='Category',
                                        ondelete='cascade',
                                        )

    stok = fields.Integer(string='Stok')
