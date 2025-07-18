from odoo import models, fields

class HrImportTimesheet(models.Model):
    _name = 'h.hr.import.timesheet'
    _description = 'Import timesheet'

    name = fields.Char(required=True)
    data_file = fields.Binary(string='Tệp dữ liệu', attachment=True)
    imported = fields.Boolean('Đã nhập')
    user_id = fields.Many2one('res.users', 'Người nhập', readonly=True, default=lambda self: self.env.user)
    import_date = fields.Datetime('Ngày nhập', default=fields.Datetime.now)
    line_ids = fields.One2many('h.hr.import.timesheet.line', 'import_id', 'Chi tiết thời gian biểu')