from odoo import models, fields

class DangKyViTri(models.Model):
    _name = 'mo_nha_an_ca.dang_ky_vi_tri'
    _description = 'Đăng ký vị trí ăn ca'

    employee_id = fields.Many2one('hr.employee', string='CBCNV', required=True)
    
    vi_tri = fields.Char(string='Vị trí ăn', required=True)
    
    ngay = fields.Date(string='Ngày', required=True)
    
    ghi_chu = fields.Text(string='Ghi chú')