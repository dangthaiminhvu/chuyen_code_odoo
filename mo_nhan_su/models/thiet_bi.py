from odoo import models, fields

class ThietBi(models.Model):
    _name = 'mo.thiet.bi'
    _description = 'Thiết bị quẹt thẻ'

    ten_thiet_bi = fields.Char(string='Tên thiết bị', required=True)
    vi_tri = fields.Char(string='Vị trí', help='Vị trí lắp đặt thiết bị')