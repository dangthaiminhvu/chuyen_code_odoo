from odoo import api, fields, models, _
from datetime import date

class CacQuyetDinhSuspendEnd(models.Model):
    _name = 'suspend.end.contract'
    _description = 'Tạm hoãn/Chấm dứt HĐ'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Mã QĐ', 
        required=True,
        copy=False, 
        readonly=True,
        default=lambda self: _('New')
    )
    employee_id = fields.Many2one(
        'hr.employee', 
        string='Nhân viên', 
        required=True,
        ondelete='restrict',
        domain=[('active', '=', True)],
        help="Chọn nhân viên áp dụng quyết định."
    )
    job_id = fields.Many2one(
        'hr.job.custom', 
        string='Chức vụ', 
        related='employee_id.job_id',
        readonly=True
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Phòng/Ban',
        related='employee_id.department_id',
        readonly=True
    )
    manager_id = fields.Many2one(
        'hr.employee',
        string='Cán bộ quản lý',
        related='employee_id.parent_id',
        readonly=True
    )

    approver_hcns_id = fields.Many2one(
        'hr.employee',
        string='TP.HCNS',
        readonly=True,
        default=lambda self: self.env['hr.employee'].search([('job_id.name', '=', 'TP.HCNS')], limit=1)
    )
    approver_director_id = fields.Many2one(
        'hr.employee',
        string='Giám đốc',
        readonly=True,
        default=lambda self: self.env['hr.employee'].search([('job_id.name', '=', 'Giám đốc')], limit=1)
    )

    decision_type = fields.Selection([
        ('suspend', 'Tạm hoãn HĐLĐ'),
        ('end', 'Chấm dứt HĐ')
    ], string='Loại', required=True, default='suspend')

    date_from = fields.Date(string='Ngày bắt đầu', required=True)
    date_to = fields.Date(string='Đến ngày')
    reason = fields.Text(string='Lý do', required=True)
    note = fields.Text(string='Ghi chú')

    checklist_line_ids = fields.One2many(
        'suspend.end.checklist',
        'suspendend_id',
        string='Danh mục công việc'
    )

    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Bị từ chối'),
    ], string='Trạng thái', default='draft', tracking=True)

    @api.depends('state')
    def _compute_button_visibility(self):
        for rec in self:
            rec.show_button_draft = rec.state != 'draft'
            rec.show_button_done = rec.state == 'draft'
            rec.show_button_cancel = rec.state == 'draft'

    show_button_draft = fields.Boolean(compute='_compute_button_visibility')
    show_button_done = fields.Boolean(compute='_compute_button_visibility')
    show_button_cancel = fields.Boolean(compute='_compute_button_visibility')

    # ✅ Các action cần thiết
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'