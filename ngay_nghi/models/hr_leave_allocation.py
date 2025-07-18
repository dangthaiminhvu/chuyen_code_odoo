from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HrLeaveAllocation(models.Model):
    _inherit = 'hr.leave.allocation'

    # Chỉ khai báo thêm trường hoặc override
    name = fields.Char(string='Mô tả phân bổ', required=True, copy=False, default=lambda self: _('New Allocation'))
    leave_type = fields.Selection([
        ('annual_leave', 'Nghỉ phép năm'),
        ('unpaid_leave', 'Nghỉ không hưởng lương'),
        ('sick_leave', 'Nghỉ ốm')],
        string='Loại ngày nghỉ', required=True)
    allocation_mode = fields.Selection([
        ('regular', 'Phân bổ thường xuyên'),
        ('accrual', 'Phân bổ dồn tích')],
        string='Chế độ phân bổ', required=True)
    date_from = fields.Date(string='Ngày bắt đầu', required=True)
    date_to = fields.Date(string='Ngày kết thúc', required=True)
    description = fields.Text(string='Mô tả')

    state = fields.Selection(
        selection_add=[
            ('approved', 'Phê duyệt'),
            ('refused', 'Từ chối'),
            ('cancelled', 'Hủy'),
        ],
        string='Trạng thái',
        tracking=True
    )

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        for rec in self:
            if rec.date_to < rec.date_from:
                raise ValidationError("Ngày kết thúc phải sau ngày bắt đầu.")

    def action_approve(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError("Chỉ có thể phê duyệt khi đang ở trạng thái Dự thảo.")
            rec.state = 'approved'

    def action_refuse(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError("Chỉ có thể từ chối khi đang ở trạng thái Dự thảo.")
            rec.state = 'refused'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'
