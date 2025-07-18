from odoo import models, fields

class FaceMachine(models.Model):
    _name = 'faceai.machine'
    _description = 'Máy chấm công khuôn mặt'
    _inherit = 'zk.machine'