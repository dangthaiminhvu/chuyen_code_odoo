from odoo import models, fields

class KhenThuongReward(models.Model):
    _name = 'khen.thuong.reward'
    _description = 'Chi tiết phần thưởng'

    khen_thuong_id = fields.Many2one('khen.thuong', string='Khen thưởng', ondelete='cascade')
    reward_type = fields.Selection([
        ('tien', 'Thưởng tiền'),
        ('vang', 'Thưởng vàng'),
        ('khac', 'Khác'),
    ], string='Phần thưởng', required=True)
    reward_name = fields.Char(string='Loại phần thưởng')
    reward_value = fields.Float(string='Giá trị')
    reward_state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('confirmed', 'Xác nhận'),
        ('done', 'Hoàn thành'),
    ], string='Trạng thái', default='draft')
