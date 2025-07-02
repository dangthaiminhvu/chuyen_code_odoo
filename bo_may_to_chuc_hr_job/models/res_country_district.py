from odoo import models, fields

class ResCountryDistrict(models.Model):
    _name = 'res.country.district'
    _description = 'Quận/Huyện'

    name = fields.Char(required=True)
    state_id = fields.Many2one('res.country.state', string='Tỉnh/Thành phố', required=True)