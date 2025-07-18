from odoo import models, fields, api
from datetime import date

class LeaveSummary(models.Model):
    _name = 'leave.summary'
    _description = 'Tổng hợp nghỉ phép'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    job_id = fields.Many2one(
        'hr.job.custom', string='Chức vụ',
        related='employee_id.job_id', store=True
    )
    department_id = fields.Many2one('hr.department.custom', string='Phòng ban')

    year = fields.Integer(string='Năm', compute='_compute_year', store=True)

    number_of_days_allocated = fields.Float(
        string='Số NP được phân bổ',
        compute='_compute_allocated', store=True
    )
    previous_year_leaves = fields.Float(
        string='Số NP năm trước chuyển sang',
        compute='_compute_prev_year', store=True
    )
    increment_by_seniority = fields.Float(
        string='Số NP tăng theo thâm niên',
        compute='_compute_seniority', store=True
    )

    used_leave_days = fields.Float(string='Số NP đã dùng')
    remaining_leave_days = fields.Float(string='Số NP còn lại', store=True)

    @api.depends('employee_id', 'year')
    def _compute_allocated(self):
        for rec in self:
            # ví dụ: lấy tổng số phép được cấp trong năm tính từ một sequence hoặc tham số HR
            # rec.number_of_days_allocated = rec.employee_id.get_allocated_days_for_year(rec.year)
            rec.number_of_days_allocated = rec.employee_id.leave_allocated or 0.0

    @api.depends('employee_id', 'year')
    def _compute_prev_year(self):
        for rec in self:
            prev = rec.year - 1
            # ví dụ: đi query summary năm trước nếu có
            prev_summary = self.search([
                ('employee_id','=',rec.employee_id.id),
                ('year','=', prev)
            ], limit=1)
            rec.previous_year_leaves = prev_summary.remaining_leave_days or 0.0

    @api.depends('employee_id')
    def _compute_seniority(self):
        for rec in self:
            if rec.employee_id.join_date:
                years = date.today().year - rec.employee_id.join_date.year
                # luật tính thâm niên: +1 ngày phép mỗi X năm?
                rec.increment_by_seniority = max(0, years - 1) * 1.0
            else:
                rec.increment_by_seniority = 0.0

    @api.depends('number_of_days_allocated', 'previous_year_leaves', 'increment_by_seniority', 'used_leave_days')
    def _compute_remaining(self):
        for rec in self:
            rec.remaining_leave_days = (
                rec.number_of_days_allocated
                + rec.previous_year_leaves
                + rec.increment_by_seniority
                - rec.used_leave_days
            )

    # ensure remaining tính lại khi thay đổi input
    _sql_constraints = [
        ('unique_emp_year', 'unique(employee_id, year)',
        "Mỗi nhân viên chỉ có 1 bản tổng hợp trong 1 năm!")
    ]
