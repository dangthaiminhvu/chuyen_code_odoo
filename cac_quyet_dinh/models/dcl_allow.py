from odoo import models, fields

class DCLAllowance(models.Model):
    _name = 'dcl.allowance'
    _description = 'Chi tiết phụ cấp'

    dcl_id = fields.Many2one('dieu.chinh.luong', ondelete='cascade')
    allowance_type = fields.Selection([
        ('xangxe','Phụ cấp xăng xe đi lại'),
        ('dienthoai','Phụ cấp điện thoại'),
        ('an','Phụ cấp ăn'),
        ('chucvu','Phụ cấp chức vụ chức danh'),
        ('trachnhiem','Phụ cấp trách nhiệm'),
        ('thamniên','Phụ cấp thâm niên'),
        ('nangnhoc','Phụ cấp nặng nhọc/ độc hại/ nguy hiểm'),
        ('other','Phụ cấp khác'),
    ], string='Phụ cấp', required=True)
    old_amount = fields.Float(string='Mức hưởng cũ', readonly=True)
    old_unit = fields.Selection([('monthly','Tháng'),('daily','Ngày')], string='Đơn vị cũ', readonly=True)
    new_amount = fields.Float(string='Mức hưởng mới')
    new_unit = fields.Selection([('monthly','Tháng'),('daily','Ngày')], string='Đơn vị mới')
