from odoo import models, fields

class HrImportTimesheetLine(models.Model):
    _name = 'h.hr.import.timesheet.line'
    _description = 'Chi tiết import timesheet'

    import_id = fields.Many2one('h.hr.import.timesheet', ondelete='cascade')
    employee_code = fields.Char('Mã nhân viên')
    barcode = fields.Char('Mã vạch')
    check_in = fields.Datetime('Chấm công vào')
    check_out = fields.Datetime('Chấm công ra')
    type = fields.Selection([('in','Vào'),('out','Ra')], 'Loại')