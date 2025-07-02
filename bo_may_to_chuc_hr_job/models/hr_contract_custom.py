from odoo import models, fields

class HrContract(models.Model):
    _inherit = 'hr.contract'

    job_id = fields.Many2one('hr.job.custom', string='Chức vụ')
    department_id = fields.Many2one('hr.department', string='Bộ phận')
