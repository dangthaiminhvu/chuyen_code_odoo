from odoo import models, fields

class DinhMucAn(models.Model):
    _name = 'mo_nha_an_ca.dinh_muc_an'
    _description = 'Định mức ăn công nghiệp'

    name = fields.Char(string='Tên định mức', required=True)
    
    nhom = fields.Selection([
        ('vanphong', 'Văn phòng'),
        ('sanxuat', 'Sản xuất'),
        # Bo sung them sau
    ], string='Nhóm CBCNV', required=True)
    
    vi_tri = fields.Char(string='Vị trí/Công việc', required=True)
    
    so_suat = fields.Integer(string='Số suất cung cấp', default=1, required=True)