from odoo import models, fields, api

class WorkTime(models.Model):
    _name = 'hr.work.time'
    _description = 'Thời gian làm việc'

    company_id = fields.Many2one('res.company', 'Công ty', default=lambda self: self.env.company)
    default_hours = fields.Float('Giờ trung bình mỗi ngày', default=8.0, readonly=True)
    min_hours = fields.Float('Giờ làm việc tối thiểu mỗi ngày', default=0.0)
    sat_days_per_month = fields.Integer('Số ngày thứ bảy làm việc mỗi tháng', default=0)
    timezone = fields.Selection([(tz, tz) for tz in ['Etc/UTC', 'Asia/Ho_Chi_Minh']], 'Múi giờ')
    line_ids = fields.One2many('hr.work.time.line', 'work_time_id', string='Giờ làm việc')