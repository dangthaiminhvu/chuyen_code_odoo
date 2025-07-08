from odoo import models, fields, api
from datetime import date

class TransferWork(models.Model):
    _name = 'lh.transfer.work'
    _description = 'Điều chuyển công tác'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # Trạng thái
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('done', 'Hoàn thành'),
    ], string='Trạng thái', default='draft', tracking=True)

    # Thông tin nhân viên
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True, tracking=True)
    job_title_old = fields.Char(string='Chức vụ', compute='_compute_old_data', store=True)
    department_old_id = fields.Many2one('hr.department', string='Phòng/Ban', compute='_compute_old_data', store=True)
    manager_old_id = fields.Many2one('hr.employee', string='Cán bộ quản lý', required=True)
    manager_old_job = fields.Char(string='Chức vụ CBQL cũ', related='manager_old_id.job_id.name', readonly=True)

    # Thông tin điều chuyển
    date_start = fields.Date(string='Thời gian áp dụng', required=True, default=lambda self: date.today())
    new_job_title = fields.Many2one('hr.job.custom', string='Chức vụ mới', required=True)
    new_department_id = fields.Many2one('hr.department', string='Phòng ban mới', required=True)
    new_manager_id = fields.Many2one('hr.employee', string='CBQL mới', required=True)
    new_manager_job = fields.Char(string='Chức vụ CBQL mới', related='new_manager_id.job_id.name', readonly=True)
    
    reason = fields.Text(string='Lý do', required=True)
    note = fields.Text(string='Ghi chú')

    # Người phê duyệt
    director_id = fields.Many2one('hr.employee', string='Giám đốc', default=lambda self: self._get_role('Giám đốc'))
    tp_hcns_id = fields.Many2one('hr.employee', string='TP.HCNS', default=lambda self: self._get_role('TP HCNS'))

    @api.depends('employee_id')
    @api.depends('employee_id')
    def _compute_old_data(self):
        for rec in self:
            rec.job_title_old = rec.employee_id.job_id.name or ''
            rec.department_old_id = rec.employee_id.department_id

    @api.model
    def _get_role(self, title):
        return self.env['hr.employee'].search([('job_title', '=', title)], limit=1).id

    transfer_status = fields.Selection([
        ('draft', 'Dự thảo'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Đã hủy'),
    ], string='Trạng thái', default='draft', tracking=True)

    def action_cancel(self):
        for rec in self:
            rec.transfer_status = 'cancel'

    def action_done(self):
        for rec in self:
            rec.transfer_status = 'done'
