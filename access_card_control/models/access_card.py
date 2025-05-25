from odoo import models, fields, api 

class AccessCard(models.Model):
    _name = 'access.card'
    _description = 'Thẻ ra vào CBCNV'

    name = fields.Char('Mã thẻ', required=True)
    employee_name = fields.Char('Tên CBCNV', required=True)
    department = fields.Char('Phòng ban')
    active = fields.Boolean('Đang hoạt động', default=True)
