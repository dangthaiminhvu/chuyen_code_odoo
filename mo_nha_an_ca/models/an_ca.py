from odoo import models, fields

class AnCa(models.Model):
    _name = 'mo_nha_an_ca.an_ca'
    _description = 'Quan ly thong tin an ca'

    employee_id = fields.Many2one('hr.employee', string='CBCNV', required=True)
    ngay = fields.Date(string='Ngay', required=True)
    ca = fields.Selection([
        ('ca1', 'Ca 1'),
        ('ca2', 'Ca 2'),
        ('ca3', 'Ca 3')], string='Ca', required=True)
    vi_tri = fields.Char(string='Vi tri an', required=True)
    trang_thai = fields.Selection([
        ('dang_an', 'Dang an'),
        ('da_ra', 'Da ra')], string='Trang thai', default='dang_an')