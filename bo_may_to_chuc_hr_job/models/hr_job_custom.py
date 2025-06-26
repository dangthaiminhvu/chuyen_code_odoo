from odoo import models, fields

class HrJobCustom(models.Model):
    _name = 'hr.job.custom'
    _description = 'Chức vụ công ty'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Chức vụ', required=True, tracking=True)
    code = fields.Char(string='Mã', tracking=True)
    working_hours = fields.Float(string='Ngưỡng thời gian', default=0.0)
    kpi_salary = fields.Float(string='KPI lương', default=0.0)

    allowance_travel = fields.Float(string='Phụ cấp đi lại', default=0.0)
    allowance_phone = fields.Float(string='Phụ cấp điện thoại', default=0.0)
    allowance_responsibility = fields.Float(string='Phụ cấp trách nhiệm', default=0.0)
    allowance_meal = fields.Float(string='Trợ cấp bữa ăn', default=0.0)
    allowance_other = fields.Float(string='Trợ cấp khác', default=0.0)

    department_id = fields.Many2one('hr.department', string='Bộ phận')
    location = fields.Text(string='Nơi làm việc')
    job_type = fields.Selection([
        ('fulltime', 'Toàn thời gian'),
        ('parttime', 'Bán thời gian'),
        ('intern', 'Thực tập'),
    ], string='Loại việc làm')
    company_id = fields.Many2one('res.company', string='Công ty', default=lambda self: self.env.company)

    objective = fields.Integer(string='Mục tiêu', default=1)
    recruiter_id = fields.Many2one('hr.employee', string='Recruiter')
    interviewer_id = fields.Many2one('hr.employee', string='Người phỏng vấn')

    description = fields.Html(string="Mô tả công việc")
    benefits    = fields.Html(string="Chế độ & phúc lợi")
