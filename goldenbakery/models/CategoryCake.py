from odoo import api, fields, models


class CategoryCake(models.Model):
    _name = 'goldenbakery.categorycake'
    _description = 'New Description'

    
    kode_categ = fields.Char(string='Kode Category')
    name = fields.Selection([
        ('cakes', 'Cakes'), 
        ('slicecakes', 'Slice Cakes'), 
        ('birthdaycake', 'Birthday Cake'), 
        ('bread', 'Bread'),
        ('dessertbox', 'Dessert Box'),
        ('pudding', 'Pudding'),
        ('cookies', 'Cookies'),
        ('traditional', 'Traditional Snack')
    ], string='Category')

    _sql_constraints = [
        ('kode_categ_unik', 'unique (kode_categ)', 'Category sudah ada !!!'),
    ]
    
    kode_chiller = fields.Char(string='Kode Chiller')
    menucake_ids = fields.One2many(comodel_name='goldenbakery.menucake', 
                                 inverse_name='categorycake_id', 
                                 string='Daftar Menu')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    daftar = fields.Char(string='Daftar Isi')
    

    @api.onchange('name')
    def _onchange_kode_categ(self):
        if (self.name == 'cakes'):
            self.kode_categ = 'CK01'
        elif (self.name == 'slicecakes'):
            self.kode_categ = 'CK02'
        elif (self.name == 'birthdaycake'):
            self.kode_categ = 'CK03'
        elif (self.name == 'bread'):
            self.kode_categ = 'CK04'
        elif (self.name == 'dessertbox'):
            self.kode_categ = 'CK05'
        elif (self.name == 'pudding'):
            self.kode_categ = 'CK06'
        elif (self.name == 'cookies'):
            self.kode_categ = 'CK07'
        elif (self.name == 'traditional'):
            self.kode_categ = 'CK08'

    
    @api.onchange('name')
    def _onchange_kode_chiller(self):
        if (self.name == 'cakes'):
            self.kode_chiller = 'CHIL01'
        elif (self.name == 'slicecakes'):
            self.kode_chiller = 'CHIL02'
        elif (self.name == 'birthdaycake'):
            self.kode_chiller = 'CHIL03'
        elif (self.name == 'bread'):
            self.kode_chiller = 'CHIL04'
        elif (self.name == 'dessertbox'):
            self.kode_chiller = 'CHIL05'
        elif (self.name == 'pudding'):
            self.kode_chiller = 'CHIL06'
        elif (self.name == 'cookies'):
            self.kode_chiller = 'CHIL07'
        elif (self.name == 'traditional'):
            self.kode_chiller = 'CHIL08'
    
    
    @api.depends('menucake_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['goldenbakery.menucake'].search([('categorycake_id', '=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a
    
