from odoo import models, fields, api, _
from datetime import timedelta

class KyLuat(models.Model):
    _name = 'ky.luat'
    _description = 'Kỷ luật'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # Trạng thái
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('confirmed', 'Xác nhận'),
        ('approved', 'Hoàn thành'),
        ('cancelled', 'Hủy'),
        ('rejected', 'Từ chối')
    ], string='Trạng thái', default='draft', tracking=True)

    # Tiêu đề kỷ luật
    title = fields.Char(string='Tiêu đề kỷ luật', required=True, tracking=True)

    # Thông tin nhân viên bị kỷ luật
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    employee_job = fields.Char(related='employee_id.job_title', string='Chức vụ', readonly=True)
    employee_department = fields.Many2one('hr.department', related='employee_id.department_id', string='Phòng ban', readonly=True)
    manager_id = fields.Many2one('hr.employee', related='employee_id.parent_id', string='CBQL', readonly=True)
    manager_department = fields.Many2one('hr.department', related='manager_id.department_id', string='Phòng ban CBQL', readonly=True)
    manager_job = fields.Char(related='manager_id.job_title', string='Chức vụ CBQL', readonly=True)

    # Người đề xuất
    proposer_id = fields.Many2one('hr.employee', string='Người đề xuất', required=True)
    proposer_department = fields.Many2one('hr.department', related='proposer_id.department_id', string='Phòng ban ND', readonly=True)
    proposer_job = fields.Char(related='proposer_id.job_title', string='Chức vụ ND', readonly=True)

    # Nội dung kỷ luật
    discipline_type = fields.Selection([
        ('noiquy', 'Kỷ luật vi phạm nội quy công ty'),
        ('baomat', 'Kỷ luật vi phạm bảo mật công ty'),
        ('khac', 'Khác')
    ], string='Loại kỷ luật', required=True)
    organizing_committee = fields.Char(string='Ban tổ chức', default=lambda self: self.env.company.name)
    date_start = fields.Date(string='Ngày bắt đầu', default=fields.Date.context_today)
    date_end = fields.Date(string='Ngày kết thúc', default=lambda self: fields.Date.context_today(self) + timedelta(days=1))
    discipline_content = fields.Text(string='Nội dung kỷ luật')

    # Quyết định
    decision_number = fields.Char(string='Số quyết định')
    approver_id = fields.Many2one('res.users', string='Người ký', readonly=True)
    approval_date = fields.Date(string='Ngày ký', readonly=True)

    # Hình phạt
    penalty_ids = fields.One2many('ky.luat.penalty', 'ky_luat_id', string='Hình phạt')

    # Tài liệu
    attachment = fields.Binary(string='Tài liệu đính kèm')
    attachment_filename = fields.Char(string='Tên tài liệu')

    # Lý do từ chối
    reject_reason = fields.Text(string='Lý do từ chối', readonly=True)

    # Actions
    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_back_to_draft(self):
        self.state = 'draft'

    def action_approve(self):
        self.write({
            'state': 'approved',
            'approver_id': self.env.user.id,
            'approval_date': fields.Date.today()
        })

    def action_reject(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lý do từ chối',
            'res_model': 'ky.luat.reject.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_ky_luat_id': self.id}
        }