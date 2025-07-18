from odoo import models, fields

class MccEmployee(models.Model):
    _name = 'mcc.employee'
    _description = 'CBCNV trên MCC'

    machine_id = fields.Many2one('zk.machine', 'Máy chấm công', required=True)
    user_type = fields.Selection([('employee','Nhân viên'),('partner','Đối tác')], 'Loại người dùng', default='employee')
    employee_id = fields.Many2one('hr.employee', 'Nhân viên', required=True)
    name = fields.Char('Tên', related='employee_id.name', readonly=True)
    mcc_uid = fields.Integer('ID trên MCC', readonly=True)
    image = fields.Binary('Ảnh')