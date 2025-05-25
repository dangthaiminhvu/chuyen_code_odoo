from odoo import models, fields, api 
from datetime import datetime

class CardSwipe(models.Model):
    _name = 'access.card.swipe'
    _description = 'Dữ liệu quẹt thẻ'

    card_id = fields.Many2one('access.card', string='Thẻ')
    swipe_time = fields.Datetime('Thời gian quẹt', default=lambda self: fields.Datetime.now())
    location = fields.Char('Vị trí')
    direction = fields.Selection([('in', 'Vào'), ('out', 'Ra')], string='Trạng thái')
    is_allowed = fields.Boolean('Đủ điều kiện vào/ra', compute='_check_access_condition', store=True)
    note = fields.Text('Ghi chú / Cảnh báo')

    @api.depends('card_id', 'direction')
    def _check_access_condition(self):
        for record in self:
            record.is_allowed = record.card_id.active
            if not record.card_id.active:
                record.note = 'Thẻ không hợp lệ hoặc đã bị khoá.'
            else:
                record.note = ''

