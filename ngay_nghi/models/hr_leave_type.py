from odoo import models, fields

class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    name = fields.Char(string="Loại nghỉ phép", required=True)
    category = fields.Selection([
        ('che_do', 'Nghỉ chế độ'),
        ('nam', 'Nghỉ phép năm'),
        ('thai_san', 'Nghỉ thai sản'),
        ('om', 'Nghỉ ốm'),
        ('khong_luong', 'Nghỉ không hưởng lương'),
        ('nghi_bu', 'Nghỉ bù'),
    ], string="Chế độ", required=True)
    
    is_unpaid = fields.Boolean(string="Nghỉ không hưởng lương", default=False)
