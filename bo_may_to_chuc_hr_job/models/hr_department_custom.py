from odoo import models, fields, api

class HrDepartmentCustom(models.Model):
    _name = 'hr.department.custom'
    _description = 'Phòng ban công ty'

    code = fields.Char(string='Mã', required=True)
    name = fields.Char(string='Tên phòng/ban', required=True)
    company_id = fields.Many2one('res.company', string='Công ty', default=lambda self: self.env.company)
    manager_id = fields.Many2one('res.users', string='Quản lý')
    parent_id = fields.Many2one('hr.department.custom', string='Phòng/Ban cấp trên')
    kpi_ratio = fields.Float(string='Tỷ lệ KPI của CBQL', digits=(6, 2))
    line_ids = fields.One2many('hr.position.assignment', 'department_id', string='Xếp hạng chức vụ')

    employee_ids = fields.One2many('hr.employee', 'department_custom_id', string='Nhân viên')
    employee_count = fields.Integer(string='Nhân viên', compute='_compute_employee_count', store=False)

    @api.depends('employee_ids')
    def _compute_employee_count(self):
        for rec in self:
            rec.employee_count = len(rec.employee_ids)
