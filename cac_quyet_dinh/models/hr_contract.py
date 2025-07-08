from odoo import models, fields

class HrContract(models.Model):
    _inherit = 'hr.contract'

    wage_type = fields.Selection([
        ('monthly', 'Theo tháng'),
        ('hourly', 'Theo giờ'),
        ('coefficient', 'Theo hệ số'),
    ], string='Loại lương')

    basic_wage = fields.Float(string='Lương cơ bản')
    kpi_wage = fields.Float(string='Lương KPI')
    labor_structure = fields.Char(string='Cấu trúc lương')
