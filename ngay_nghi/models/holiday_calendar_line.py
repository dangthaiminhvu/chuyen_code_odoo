from odoo import models, fields


class HolidayCalendarLine(models.Model):
    _name = 'holiday.calendar.line'
    _description = 'Holiday Calendar Line'
    _order = 'date_start'

    name = fields.Char(string='Tên', required=True)
    date_start = fields.Date(string='Ngày bắt đầu', required=True)
    date_end = fields.Date(string='Ngày kết thúc', required=True)
    working_hours_type = fields.Selection([
        ('standard_40', 'Standard 40 hours/week'),
        ('standard_40_sat', 'Standard 40 hours/week (Làm thứ 7)')
    ], string='Giờ làm việc', required=True, default='standard_40')

    work_type = fields.Selection([
        ('overtime', 'Giờ tăng ca'),
        ('attendance', 'Chuyên cần')
    ], string='Loại công việc', required=True, default='attendance')
