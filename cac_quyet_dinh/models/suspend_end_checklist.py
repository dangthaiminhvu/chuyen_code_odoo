from odoo import fields, models

class CacQuyetDinhSuspendEndChecklist(models.TransientModel):
    _name = 'suspend.end.checklist'
    _description = 'Checklist Tạm hoãn/Chấm dứt HĐ'

    suspendend_id = fields.Many2one(
        'cac.quyetdinh.suspendend',
        string='Quyết định',
        ondelete='cascade'
    )
    content = fields.Text(string='Nội dung', required=True)
    recipient_id = fields.Many2one('hr.employee', string='Người nhận')
    department_id = fields.Many2one('hr.department', string='Phòng/Ban')
    job_id = fields.Many2one('hr.job', string='Chức vụ')
    date_done = fields.Date(string='Ngày hoàn thành')
    note = fields.Text(string='Ghi chú')
    is_employee = fields.Boolean(string='Is Employee')
    is_responsible = fields.Boolean(string='Is Responsible')
    state = fields.Selection([
        ('draft','Dự thảo'),
        ('done','Hoàn thành'),
    ], string='Trạng thái', default='draft')

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
