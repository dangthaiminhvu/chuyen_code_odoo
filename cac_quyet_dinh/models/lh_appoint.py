from odoo import models, fields, api
from datetime import date

class Appoint(models.Model):
    _name = 'lh.appoint'
    _description = 'Bổ nhiệm / Miễn nhiệm'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'
    
    name = fields.Char(string='Số quyết định', required=True, copy=False, readonly=True, default='Mới')

    # Trạng thái xử lý
    transfer_status = fields.Selection([
        ('draft', 'Dự thảo'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Đã hủy'),
    ], string='Trạng thái', default='draft', tracking=True)
    
    decision_type = fields.Selection([
        ('bo_nhiem', 'Bổ nhiệm'),
        ('mien_nhiem', 'Miễn nhiệm'),
    ], string='Loại quyết định', default='bo_nhiem', tracking=True)

    # Nhân viên cũ
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True, tracking=True)
    old_job_title = fields.Char(string='Chức vụ', compute='_compute_old_data', store=True)
    old_department_id = fields.Many2one('hr.department', string='Phòng/Ban', compute='_compute_old_data', store=True)
    old_manager_id = fields.Many2one('hr.employee', string='Cán bộ quản lý', required=True)
    old_manager_job = fields.Char(string='Chức vụ', related='old_manager_id.job_id.name', readonly=True)

    # Thông tin mới
    date_start = fields.Date(string='Từ ngày', required=True, default=lambda self: date.today())
    new_job_title = fields.Many2one('hr.job.custom', string='Chức vụ mới', required=True)
    new_manager_id = fields.Many2one('hr.employee', string='CBQL mới')
    new_manager_job = fields.Char(string='Chức vụ', related='new_manager_id.job_id.name', readonly=True)
    reason = fields.Text(string='Lý do', required=True)
    note = fields.Text(string='Ghi chú')

    # Người phê duyệt
    director_id = fields.Many2one('hr.employee', string='Giám đốc', default=lambda self: self._get_role('Giám đốc'))
    tp_hcns_id = fields.Many2one('hr.employee', string='TP.HCNS', default=lambda self: self._get_role('TP HCNS'))

    # Người thông báo
    notify_ids = fields.Selection([
        ('nhan_vien', 'Nhân viên'), 
        ('moi_nguoi', 'Tất cả người dùng nội bộ'), 
        ('phong_ban', 'Phòng ban'),
    ], string='Thông báo', default='nhan_vien', tracking=True)
    show_notify_employee = fields.Boolean(string='Hiện người nhận thông báo', compute='_compute_show_notify_employee')
    notify_employee_id = fields.Many2one('hr.employee', string='Nhân viên nhận thông báo')


    @api.depends('employee_id')
    def _compute_old_data(self):
        for rec in self:
            rec.old_job_title = rec.employee_id.job_id.name or ''
            rec.old_department_id = rec.employee_id.department_id

    @api.model
    def _get_role(self, title):
        return self.env['hr.employee'].search([('job_title', '=', title)], limit=1).id

    def action_done(self):
        for rec in self:
            rec.transfer_status = 'done'

    def action_cancel(self):
        for rec in self:
            rec.transfer_status = 'cancel'
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Mới') == 'Mới':
            vals['name'] = self.env['ir.sequence'].next_by_code('lh.appoint') or 'Mới'
        return super(Appoint, self).create(vals)

    @api.depends('notify_ids')
    def _compute_show_notify_employee(self):
        for rec in self:
            rec.show_notify_employee = rec.notify_ids == 'nhan_vien'

