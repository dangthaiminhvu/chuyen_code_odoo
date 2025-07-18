from odoo import models, fields

class LyDoNghiViec(models.Model):
    _name = 'ly.do.nghi.viec'
    _description = 'Lý do nghỉ việc'

    name = fields.Char(string="Lý do nghỉ việc", required=True)