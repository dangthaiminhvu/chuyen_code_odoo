from odoo import models, fields, api

class KyLuatPenalty(models.Model):
    _name = 'ky.luat.penalty'
    _description = 'Chi tiết hình phạt'

    ky_luat_id = fields.Many2one('ky.luat', string='Kỷ luật', ondelete='cascade')
    penalty_type = fields.Selection([
        ('tien', 'Phạt tiền'),
        ('dinhchi', 'Đình chỉ công tác một ngày'),
        ('khac', 'Khác')
    ], string='Hình phạt', required=True)
    penalty_method = fields.Char(string='Loại hình phạt')
    penalty_value = fields.Float(string='Giá trị')
    penalty_state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('confirmed', 'Xác nhận'),
        ('done', 'Hoàn thành')
    ], string='Trạng thái', default='draft')

    @api.onchange('penalty_type')
    def _onchange_penalty_type(self):
        if self.penalty_type == 'tien':
            self.penalty_method = 'Tiền mặt'
        elif self.penalty_type == 'dinhchi':
            self.penalty_method = 'Đình chỉ công tác'
        else:
            self.penalty_method = False
