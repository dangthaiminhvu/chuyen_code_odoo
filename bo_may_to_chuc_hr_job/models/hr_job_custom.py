from odoo import models, fields, api    
import logging

_logger = logging.getLogger(__name__)
_logger.warning(">>> ĐÃ LOAD MODEL hr.job.custom <<<")


class HrJobCustom(models.Model):
    _name = 'hr.job.custom'
    _description = 'Chức vụ công ty'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    employee_current = fields.Integer(string='Số nhân viên hiện tại', compute='_compute_employee_stats', store=True)
    employee_target = fields.Integer(string='Tổng số nhân viên dự kiến', compute='_compute_employee_stats', store=True)
    employee_hired = fields.Integer(string='Nhân viên được tuyển', compute='_compute_employee_stats', store=True)

    name = fields.Char(string='Chức vụ', required=True, tracking=True)
    code = fields.Char(string='Mã', required=True, tracking=True)
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
    requirements = fields.Html(string='Yêu Cầu')

    @api.model
    def _get_default_composer_context(self):
        return {
            'default_composition_mode': 'comment',
            'default_use_signature': True,
        }
        
    @api.depends('objective')
    def _compute_employee_stats(self):
        Employee = self.env['hr.employee']
        for job in self:
            employees = Employee.search([('job_id', '=', job.id)])
            job.employee_current = len(employees.filtered(lambda e: e.active))
            job.employee_target = job.objective + len(employees)
            job.employee_hired = len(employees.filtered(lambda e: e.is_recruited))

    def action_add_note(self):
        """ Mở wizard ghi chú nội bộ """
        return {
            'name': 'Thêm ghi chú',
            'type': 'ir.actions.act_window',
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'view_id': self.env.ref('mail.view_compose_message_wizard_form').id,
            'target': 'new',
            'context': dict(self._get_default_composer_context(), **{
                'default_res_model': self._name,
                'default_res_id': self.id,
            }),
        }