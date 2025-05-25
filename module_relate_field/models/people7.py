from odoo import models, fields, api # type: ignore


class People(models.Model):
    _name = 'people7'
    _description = 'People7'

    name = fields.Char(string='Name')