from datetime import date
from odoo import models, fields  

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    job_id = fields.Many2one('hr.job.custom', string='Chức vụ')
    is_recruited = fields.Boolean(string='Đã được tuyển')
    department_custom_id = fields.Many2one('hr.department.custom', string='Phòng ban')

    status = fields.Selection([
        ('working', 'Đang làm việc'),
        ('maternity', 'Nghỉ thai sản'),
        ('terminated', 'Đã nghỉ việc'),
    ], string='Trạng thái', default='working')
    
    first_contract_date = fields.Date(string="Ngày bắt đầu làm việc") 
    seniority = fields.Char(string='Thâm niên', compute='_compute_seniority', store=True)

    def _compute_seniority(self):
        for rec in self:
            if rec.first_contract_date:
                today = date.today()
                delta = today - rec.first_contract_date
                years = delta.days // 365
                months = (delta.days % 365) // 30
                rec.seniority = f"{years} năm {months} tháng"
            else:
                rec.seniority = "Chưa có hợp đồng"
                
    employee_id = fields.Many2one(
        'hr.employee',
        string='Liên kết nhân viên',
        compute='_compute_employee_id',
        store=True,
    )

    def _compute_employee_id(self):
        for rec in self:
            rec.employee_id = rec

