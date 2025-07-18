from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date

class KhenThuong(models.Model):
    _name = 'khen.thuong'
    _description = 'Khen thưởng'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # Tiêu đề khen thưởng
    title = fields.Char(string = "Tiêu đề khen thưởng")
    
    # Trạng thái
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('confirmed', 'Xác nhận'),
        ('approved', 'Hoàn thành'),
        ('cancelled', 'Hủy'),
        ('rejected', 'Từ chối')
    ], string='Trạng thái', default='draft', tracking=True)

    # Thông tin nhân viên được khen thưởng
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    job_title = fields.Char(string='Chức vụ', related='employee_id.job_title', readonly=True)
    department_id = fields.Many2one('hr.department', string='Phòng ban', related='employee_id.department_id', readonly=True)
    manager_id = fields.Many2one('hr.employee', string='CBQL', related='employee_id.parent_id', readonly=True)

    # Người đề xuất
    proposer_id = fields.Many2one('hr.employee', string='Người đề xuất', required=True)
    proposer_department = fields.Many2one('hr.department', string='Phòng ban', related='proposer_id.department_id', readonly=True)
    proposer_job = fields.Char(string='Chức vụ', related='proposer_id.job_title', readonly=True)
    propose_date = fields.Date(string='Ngày đề xuất', default=fields.Date.context_today)

    # Nội dung khen thưởng
    award_type = fields.Selection([
        ('nam', 'Khen thưởng CBNV xuất sắc của năm'),
        ('thang', 'Khen thưởng CBNV xuất sắc của tháng')
    ], string='Khen thưởng', required=True)
    organizing_committee = fields.Char(string='Ban tổ chức')
    award_content = fields.Text(string='Nội dung khen thưởng')

    # Quyết định
    decision_number = fields.Char(string='Số quyết định')
    approver_id = fields.Many2one('res.users', string='Người ký', readonly=True)
    approval_date = fields.Date(string='Ngày ký', readonly=True)

    # Phần thưởng
    reward_ids = fields.One2many('khen.thuong.reward', 'khen_thuong_id', string='Phần thưởng')

    # Tài liệu đính kèm
    attachment = fields.Binary(string='Tài liệu đính kèm')
    attachment_filename = fields.Char(string="Tên tài liệu")

    # Lý do từ chối
    reject_reason = fields.Text(string='Lý do từ chối', readonly=True)

    # Button Actions
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
            'res_model': 'khen.thuong.reject.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_khen_thuong_id': self.id}
        }