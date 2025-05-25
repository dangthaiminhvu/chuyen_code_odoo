from odoo import models, fields

class NhanSu(models.Model):
    _inherit = 'hr.employee'

    ma_the = fields.Char(string='Mã thẻ', help='Mã thẻ RFID của nhân viên')
    ca_lam_viec_id = fields.Many2one('mo.ca.lam.viec', string='Ca làm việc', help='Ca làm việc hiện tại')