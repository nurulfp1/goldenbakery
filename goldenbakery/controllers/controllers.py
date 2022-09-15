from odoo import http, models, fields
from odoo.http import request
import json

class goldenbakery(http.Controller):
    @http.route('/goldenbakery/getmenucake', auth='public', method=['GET'])
    def getmenucake(self, **kw):
        menucake = request.env['goldenbakery.menucake'].search([])
        isi = []
        for mc in menucake:
            isi.append({
                'nama_menucake' : mc.name,
                'harga_jual' : mc.harga_jual,
                'stok' : mc.stok
            })
        return json.dumps(isi)

    @http.route('/goldenbakery/getsupplier', auth='public', method=['GET'])
    def getsupplier(self, **kw):
        supplier = request.env['goldenbakery.supplier'].search([])
        isi = []
        for sp in supplier:
            isi.append({
                'nama_supplier' : sp.name,
                'alamat' : sp.alamat,
                'no_telp' : sp.no_telp,
                'rawingridient' : sp.rawingridient_id[0].name
            })
        return json.dumps(isi)

    @http.route('/goldenbakery/getrawingridient', auth='public', method=['GET'])
    def getrawingridient(self, **kw):
        rawingridient = request.env['goldenbakery.rawingridient'].search([])
        isi = []
        for ri in rawingridient:
            isi.append({
                'nama_rawingridient' : ri.name,
                'unit' : ri.unit,
                'harga_beli' : ri.harga_beli,
                'stok' : ri.stok,
                'supplier' : ri.supplier_id[0].name
            })
        return json.dumps(isi)
