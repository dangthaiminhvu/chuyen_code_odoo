from odoo import models, fields

class CaLamViec(models.Model):
    _name = 'mo.ca.lam.viec'
    _description = 'Ca làm việc'

    ten_ca = fields.Char(string='Tên ca', required=True)
    gio_bat_dau = fields.Float(string='Giờ bắt đầu', help='Giờ bắt đầu ca')
    gio_ket_thuc = fields.Float(string='Giờ kết thúc', help='Giờ kết thúc ca')