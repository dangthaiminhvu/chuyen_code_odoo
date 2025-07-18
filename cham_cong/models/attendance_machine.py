from odoo import models, fields, api

class ZkMachine(models.Model):
    _name = 'zk.machine'
    _description = 'Máy chấm công'

    name = fields.Char('Tên máy chấm công', required=True)
    serial = fields.Char('Seri MCC')
    location = fields.Char('Vị trí MCC')
    port = fields.Integer('Số port', default=0)
    company_id = fields.Many2one('res.company', 'Công ty', default=lambda self: self.env.company)
    mcc_type = fields.Selection([('finger', 'Vân tay'), ('face', 'Khuôn mặt')], 'Loại máy')

    def test_connection(self):
        # placeholder
        return True

    def reboot_machine(self):
        # placeholder
        return True

    def create_account(self):
        # placeholder
        return True