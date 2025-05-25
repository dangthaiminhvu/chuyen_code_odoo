from odoo import models, fields # type: ignore


class People4(models.Model):
    _name = 'people4'
    _description = 'People4'

    name = fields.Char(string='Name')

    # One2many field
    house_ids = fields.One2many('house', 'people4_id', string='House')