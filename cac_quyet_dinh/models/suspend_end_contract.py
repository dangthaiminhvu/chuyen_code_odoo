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
        'hr.job', 
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
        'cac.quyetdinh.suspendend.checklist',
        'suspendend_id',
        string='Danh mục công việc'
    )

    state = fields.Selection([
        ('draft','Dự thảo'),
        ('done','Hoàn thành'),
        ('cancel','Bị Từ chối')
    ], string='Trạng thái', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq = self.env['ir.sequence'].next_by_code('cac.quyetdinh.suspendend') or _('New')
            vals['name'] = seq
        return super().create(vals)
