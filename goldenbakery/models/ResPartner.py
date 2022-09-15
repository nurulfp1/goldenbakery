from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    
    is_customer = fields.Boolean(string='Is Customer')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')