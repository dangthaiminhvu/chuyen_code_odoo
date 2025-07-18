from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CacQuyetDinhTransferLine(models.Model):
    _name = 'cac.quyetdinh.transfer.line'
    _description = 'Chi tiết đánh giá'

    transfer_id    = fields.Many2one('cac.quyetdinh.renew.contract', ondelete='cascade')
    name           = fields.Char('Tiêu chí')
    criterion_type = fields.Selection([
        ('title', 'Tiêu đề'),
        ('sub', 'Tiêu chí con'),
        ('normal', 'Tiêu chí thường')
    ], string='Loại tiêu chí', default='normal')
    max_score      = fields.Float('Điểm tối đa')
    score          = fields.Float('Điểm CBNV đánh giá')
    manager_score  = fields.Float('Kết quả CBQL đánh giá')
    description    = fields.Text('Ghi chú')
    state          = fields.Selection([
        ('draft', 'Bản nháp'),
        ('done', 'Hoàn thành')
    ], default='draft', string='Trạng thái')
    
    is_title = fields.Boolean(string='Is Title', compute='_compute_flags', store=True)
    is_subfolder = fields.Boolean(string='Is Subfolder', compute='_compute_flags', store=True)
    is_employee = fields.Boolean(string='Is Employee', default=False)
    is_manager = fields.Boolean(string='Is Manager', default=False)

    @api.depends('criterion_type')
    def _compute_flags(self):
        for rec in self:
            rec.is_title = rec.criterion_type == 'title'
            rec.is_subfolder = rec.criterion_type == 'sub'
            
    @api.constrains('score', 'manager_score', 'max_score')
    def _check_score_limits(self):
        for rec in self:
            if rec.score and rec.max_score and rec.score > rec.max_score:
                raise ValidationError("Điểm CBNV không được vượt quá điểm tối đa.")
            if rec.manager_score and rec.max_score and rec.manager_score > rec.max_score:
                raise ValidationError("Điểm CBQL không được vượt quá điểm tối đa.")
