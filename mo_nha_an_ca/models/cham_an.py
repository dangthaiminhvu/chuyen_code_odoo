from odoo import models, fields

class ChamAn(models.Model):
    _name = 'mo_nha_an_ca.cham_an'
    _description = 'Chấm số suất ăn thực tế'

    phieu_quet_id = fields.Many2one('mo_nha_an_ca.phieu_quet_the', string='Phiếu quẹt thẻ')
    bao_an_id = fields.Many2one('mo_nha_an_ca.bao_an', string='Báo ăn', required=True)
    so_suat_thuc_te = fields.Integer(string='Số suất thực tế', default=0)
    ly_do = fields.Text(string='Lý do (ngoại lệ)')