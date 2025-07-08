from odoo import models, fields, api

class KhenThuongRejectWizard(models.TransientModel):
    _name = 'khen.thuong.reject.wizard'
    _description = 'Wizard lý do từ chối khen thưởng'

    khen_thuong_id = fields.Many2one('khen.thuong', string='Khen thưởng', required=True)
    reason = fields.Text(string='Lý do từ chối', required=True)

    def action_submit_reject(self):
        self.khen_thuong_id.write({
            'state': 'rejected',
            'reject_reason': self.reason,
        })
