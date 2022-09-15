from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Transaksi(models.Model):
    _name = 'goldenbakery.transaksi'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_transaksi = fields.Datetime(string='Tgl. Transaksi', default=fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailtransaksi_ids = fields.One2many(
        comodel_name='goldenbakery.detailtransaksi', 
        inverse_name='transaksi_id', 
        string='Detail Transaksi',)

    
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'), 
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancel', 'Cancelled'),
                   ],
        required="True", readonly=True, default="draft")
    

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_draft(self):
        self.write({'state': 'draft'})


    @api.depends('detailtransaksi_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['goldenbakery.detailtransaksi'].search([('transaksi_id', '=',rec.id)]).mapped('subtotal'))
        rec.total_bayar = a
    

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("Tidak dapat dihapus jika status BUKAN DRAFT")
        if self.detailtransaksi_ids:
            a = []
            for rec in self:
                a = self.env['goldenbakery.detailtransaksi'].search([('transaksi_id', '=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.menucake_id.name) + ' ' + str(ob.qty))
                ob.menucake_id.stok += ob.qty
        record = super(Transaksi,self).unlink()

    def write(self,vals):
        for rec in self:
            a = self.env['goldenbakery.detailtransaksi'].search([('transaksi_id', '=',rec.id)])
            print(a)
            for data in a:
                print(str(data.menucake_id.name)+' '+str(data.qty)+' '+str(data.menucake_id.stok))
                data.menucake_id.stok += data.qty
        record = super(Transaksi,self).write(vals)
        for rec in self:
            b = self.env['goldenbakery.detailtransaksi'].search([('transaksi_id', '=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.menucake_id.name)+' '+str(databaru.qty)+' '+str(databaru.menucake_id.stok))
                    databaru.menucake_id.stok -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama !!!'),
    ]

    @api.depends('detailtransaksi_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['goldenbakery.detailtransaksi'].search([('transaksi_id', '=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a


class DetailTransaksi(models.Model):
    _name = 'goldenbakery.detailtransaksi'
    _description = 'New Description'

    name = fields.Char(string='Name')
    transaksi_id = fields.Many2one(comodel_name='goldenbakery.transaksi', string='Detail Transaksi')
    menucake_id = fields.Many2one(comodel_name='goldenbakery.menucake', string='List Cake')
    harga_satuan = fields.Integer(string='Harga')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
        

    @api.onchange('menucake_id')
    def _onchange_menucake_id(self):
        if (self.menucake_id.harga_jual):
            self.harga_satuan = self.menucake_id.harga_jual
        
    @api.model
    def create(self, vals):
        record = super(DetailTransaksi,self).create(vals)
        if record.qty:
            self.env['goldenbakery.menucake'].search([('id', '=',record.menucake_id.id)]).write({'stok' : record.menucake_id.stok - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau belanja {} berapa banyak sihh..".format(rec.menucake_id.name))
            elif (rec.menucake_id.stok < rec.qty):
                raise ValidationError("Stok {} tidak mencukupi, hanya tersedia {}".format(rec.menucake_id.name, rec.menucake_id.stok))
