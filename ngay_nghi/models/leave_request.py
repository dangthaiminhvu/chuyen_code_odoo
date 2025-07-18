from odoo import models, fields, api, _

class LeaveRequest(models.Model):
    _name = 'leave.request'
    _description = 'Ngày nghỉ'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Mã', required=True, copy=False, readonly=True, default='New')
    
    regime = fields.Selection([
        ('annual_leave', 'Nghỉ phép năm'),
        ('unpaid_leave', 'Nghỉ không hưởng lương'),
        ('sick_leave', 'Nghỉ ốm'),
        ('maternity_leave', 'Nghỉ thai sản'),
        ('regime_leave', 'Nghỉ chế độ'),
        ('compensatory_leave', 'Nghỉ bù'),
    ], string='Chế độ', required=True)

    leave_type_id = fields.Many2one('hr.leave.type', string='Loại ngày nghỉ', required=True)

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)

    date_from = fields.Date(string='Từ')
    date_to = fields.Date(string='Đến')

    half_day = fields.Boolean(string='Nửa ngày')
    half_day_type = fields.Selection([
        ('morning', 'Buổi sáng'),
        ('afternoon', 'Buổi chiều'),
    ], string='Buổi')

    reason = fields.Text(string='Lý do')
    attachment = fields.Binary(string='Tệp đính kèm')
    attachment_filename = fields.Char(string='Tên tệp')

    handover_to = fields.Many2one('hr.employee', string='Người nhận bàn giao')
    handover_date = fields.Date(string='Ngày bàn giao', default=fields.Date.today)

    notify_target = fields.Selection([
        ('employee', 'Nhân viên'),
        ('department', 'Phòng ban'),
        ('all', 'Tất cả'),
    ], string='Đối tượng thông báo')

    notify_employee = fields.Many2one('hr.employee', string='Nhân viên thông báo')
    notify_department = fields.Many2one('hr.department.custom', string='Phòng ban thông báo')

    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('waiting', 'Chờ CBQL phê duyệt'),
        ('approved', 'Hoàn thành'),
        ('refused', 'Bị từ chối'),
        ('cancelled', 'Hủy'),
    ], string='Trạng thái', default='draft', tracking=True)

    show_half_day_type = fields.Boolean(
        compute='_compute_half_day_type_visibility',
        store=True
    )
    show_notify_employee = fields.Boolean(
        compute='_compute_notify_fields',
        store=True
    )
    show_notify_department = fields.Boolean(
        compute='_compute_notify_fields',
        store=True
    )

    @api.depends('half_day')
    def _compute_half_day_type_visibility(self):
        for rec in self:
            rec.show_half_day_type = rec.half_day

    @api.depends('notify_target')
    def _compute_notify_fields(self):
        for rec in self:
            rec.show_notify_employee = rec.notify_target == 'employee'
            rec.show_notify_department = rec.notify_target == 'department'

    @api.onchange('regime')
    def _onchange_regime(self):
        return {
            'domain': {
                'leave_type_id': [('category', '=', self.regime)]
            }
        }

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('leave.request') or 'New'
        return super().create(vals)

    def action_confirm(self):
        self.state = 'waiting'

    def action_approve(self):
        self.state = 'approved'

    def action_refuse(self):
        self.state = 'refused'

    def action_cancel(self):
        self.state = 'cancelled'