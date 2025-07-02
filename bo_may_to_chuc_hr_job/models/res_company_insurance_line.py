from odoo import models, fields

class ResCompanyInsuranceLine(models.Model):
    _name = 'res.company.insurance.line'
    _description = 'Dòng thông tin bảo hiểm'

    company_id = fields.Many2one(
        'res.company.custom', string='Công ty', ondelete='cascade'
    )
    insurance_serial = fields.Char(string='Serial')
    insurance_provider = fields.Char(string='Nhà cung cấp')
    insurance_format = fields.Char(string='Định dạng')
    insurance_start_date = fields.Date(string='Ngày bắt đầu')
    insurance_end_date = fields.Date(string='Ngày kết thúc')
