from odoo import models, fields

class CacQuyetDinhChallenge(models.Model):
    _name = 'cac.quyetdinh.challenge'
    _description = 'Thử thách'

    transfer_id    = fields.Many2one('cac.quyetdinh.renew.contract', ondelete='cascade')
    challenge_name = fields.Char(string='Tên thử thách', required=True)
    total_score    = fields.Float(string='Tổng đánh giá', digits=(6, 2))
    state          = fields.Selection([
        ('not_started', 'Chưa bắt đầu'),
        ('in_progress', 'Đang thực hiện'),
        ('done', 'Hoàn thành'),
        ('failed', 'Không đạt')
    ], string='Trạng thái', default='not_started')
