from odoo import models, fields

class KyLuatRejectWizard(models.TransientModel):
    _name = 'ky.luat.reject.wizard'
    _description = 'Wizard lý do từ chối kỷ luật'

    ky_luat_id = fields.Many2one('ky.luat', string='Kỷ luật', required=True)
    reason = fields.Text(string='Lý do từ chối', required=True)

    def action_submit_reject(self):
        self.ky_luat_id.write({
            'state': 'rejected',
            'reject_reason': self.reason,
        })