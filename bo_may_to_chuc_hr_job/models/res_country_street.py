from odoo import models, fields

class ResCountryStreet(models.Model):
    _name = 'res.country.street'
    _description = 'Đường'

    name = fields.Char(required=True)
    district_id = fields.Many2one('res.country.district', string='Quận/Huyện', required=True)