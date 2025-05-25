from odoo import models, fields

class DangKySuatAn(models.Model):
    _name = 'mo_nha_an_ca.dang_ky_suat_an'
    _description = 'Đăng ký suất ăn'

    employee_id = fields.Many2one('hr.employee', string='CBCNV', required=True)
    
    dinh_muc_id = fields.Many2one('mo_nha_an_ca.dinh_muc_an', string='Định mức', required=True)
    
    ngay = fields.Date(string='Ngày', required=True)
    
    so_suat = fields.Integer(string='Số suất đăng ký', default=1)
    
    loai_suat = fields.Selection([
        ('chinh', 'Suất ăn chính'),
        ('phu', 'Suất ăn phụ'),
    ], string='Loại suất ăn', default='chinh')