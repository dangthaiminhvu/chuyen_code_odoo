from odoo import models, fields

class AttendanceData(models.Model):
    _name = 'log.attendance'
    _description = 'Dữ liệu chấm công'

    employee_id = fields.Many2one('hr.employee', 'Nhân viên')
    mcc_uid = fields.Integer('ID trên MCC')
    machine_serial = fields.Char('Seri MCC')
    check_time = fields.Datetime('Thời gian chấm công')
    date = fields.Date('Ngày')
    image = fields.Binary('Hình ảnh chấm công')