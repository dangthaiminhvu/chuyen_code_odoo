from odoo import models, fields # type: ignore


class People2(models.Model):
    _inherit = 'people2'

    name = fields.Char(string='Name')

    # Selection field
    gender = fields.Selection(selection_add=[('gay', 'Gay')], ondelete={'gay': 'set null'})
