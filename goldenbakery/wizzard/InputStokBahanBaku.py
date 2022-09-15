from odoo import api, fields, models


class InputStokBahanBaku(models.Model):
    _name = 'goldenbakery.inputstokbahanbaku'

    rawingridient_id = fields.Many2one(
        comodel_name='goldenbakery.rawingridient', 
        string='Nama',
        required=True)
    
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    
    def button_input_stok_bahan_baku(self):
        for rec in self:
            self.env['goldenbakery.rawingridient'].search([('id', '=', rec.rawingridient_id.id)]).write({'stok' : rec.rawingridient_id.stok + rec.jumlah})