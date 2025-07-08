from odoo import models, fields

class DCLRejectWizard(models.TransientModel):
    _name = 'dcl.reject.wizard'
    _description = 'Wizard lý do từ chối điều chỉnh lương'

    dcl_id = fields.Many2one('dieu.chinh.luong', string='Điều chỉnh lương', required=True)
    reason_type = fields.Selection([('request_edit','Yêu cầu chỉnh sửa'),('request_reject','Yêu cầu từ chối')], string='Lý do', required=True)
    description = fields.Text(string='Mô tả', required=True)

    def action_submit_reject(self):
        self.dcl_id.write({'state':'rejected'})