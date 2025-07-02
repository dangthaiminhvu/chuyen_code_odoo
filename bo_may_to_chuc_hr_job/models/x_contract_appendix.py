from odoo import models, fields, api

class ContractAppendix(models.Model):
    _name = 'x.contract.appendix'
    _description = 'Contract Appendix'

    name = fields.Char(string='Phụ lục', required=True)
    contract_id = fields.Many2one('hr.contract', string='Hợp đồng', required=True)
    employee_id = fields.Many2one('hr.employee', string='Nhân viên')
    job_id = fields.Many2one(related='employee_id.job_id', string="Chức vụ", readonly=True, store=True)
    department_id = fields.Many2one(related='contract_id.department_id', store=True)
    effective_date = fields.Date(string='Ngày hiệu lực', required=True)
    attachment = fields.Binary(string='Đính kèm', attachment=True)
    filename = fields.Char(string='Tên tệp')

    allowance_lines = fields.One2many('x.contract.appendix.allowance', 'appendix_id', string='Thông tin phụ cấp')

    salary_type = fields.Selection([
        ('gross', 'Lương Gross'),
        ('net', 'Lương Net'),
    ], string='Loại lương')

    wage = fields.Float(string='Lương thỏa thuận')
    wage_kpi = fields.Float(string='Lương KPI')
    wage_basic = fields.Float(string='Lương cơ bản')
    wage_bhxh = fields.Float(string='Lương đóng BHXH')

    structure_type_id = fields.Many2one('hr.payroll.structure.type', string='Cấu trúc lương')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'x_contract_appendix_attachment_rel',
        'appendix_id',
        'attachment_id',
        string="Tệp đính kèm",
        domain=[('res_model', '=', 'x.contract.appendix')],
        context={'default_res_model': 'x.contract.appendix', 'default_res_id': lambda self: self.id},
    )

    state = fields.Selection([
        ('draft', 'Mới'),
        ('running', 'Đang chạy'),
        ('paused', 'Tạm hoãn HĐ'),
        ('expired', 'Hết hiệu lực'),
    ], string='Trạng thái', default='draft', required=True)
    
    @api.model
    def _default_state(self):
        return "draft"

    def action_set_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_set_running(self):
        for rec in self:
            rec.state = "running"

    def action_set_expired(self):
        for rec in self:
            rec.state = "expired"

    def action_set_canceled(self):
        for rec in self:
            rec.state = "canceled"
