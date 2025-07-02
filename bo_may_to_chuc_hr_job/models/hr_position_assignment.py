from odoo import models, fields

class HrDepartmentCustomLine(models.Model):
    _name = 'hr.position.assignment'
    _description = 'Chi tiết chức vụ trong phòng ban'

    department_id = fields.Many2one('hr.department.custom', string='Phòng ban', ondelete='cascade')
    job_id = fields.Many2one('hr.job.custom', string='Chức vụ')
    is_manager = fields.Boolean(string='Là người quản lý')
    employee_id = fields.Many2one('hr.employee', string='Cán bộ quản lý')
    ranking = fields.Integer(string='Xếp hạng chức vụ')
    active = fields.Boolean(string='Có hiệu lực', default=True)
