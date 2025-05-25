from odoo import models, fields

class BaoAn(models.Model):
    _name = 'mo_nha_an_ca.bao_an'
    _description = 'Báo ăn ca'

    ngay = fields.Date(string='Ngày', required=True)
    
    ca = fields.Selection([
        ('ca1','Ca 1'),
        ('ca2','Ca 2'),
        ('ca3','Ca 3')], string='Ca làm việc', required=True)
    
    vi_tri = fields.Char(string='Vị trí ăn', required=True)
    
    so_suat_du_kien = fields.Integer(string='Số suất dự kiến', default=0)
    
    doi_tac_ngoai = fields.Integer(string='Suất ăn khách ngoài', default=0)