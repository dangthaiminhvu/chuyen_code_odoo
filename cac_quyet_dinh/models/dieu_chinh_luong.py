from odoo import models, fields, api
from datetime import date

class DieuChinhLuong(models.Model):
    _name = 'dieu.chinh.luong'
    _description = 'Điều chỉnh lương'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # trạng thái
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('waiting_hcns', 'Chờ TP.HCNS duyệt'),
        ('done', 'Hoàn thành'),
        ('rejected', 'Bị từ chối'),
        ('cancelled', 'Hủy'),
    ], string='Trạng thái', default='draft', tracking=True)

    # Thông tin nhân viên
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True, tracking=True)
    job_title = fields.Char(related='employee_id.job_title', string='Chức vụ', readonly=True)
    department_id = fields.Many2one('hr.department', related='employee_id.department_id', string='Phòng ban', readonly=True)
    manager_id = fields.Many2one('hr.employee', string='Cán bộ quản lý', required=True)
    manager_job = fields.Char(related='manager_id.job_title', string='Chức vụ CBQL', readonly=True)

    # Thông tin phê duyệt
    tp_hcns_id = fields.Many2one('hr.employee', string='TP. HCNS', default=lambda self: self._get_role('TP HCNS'))
    cfo_id = fields.Many2one('hr.employee', string='Giám đốc Tài chính', default=lambda self: self._get_role('Giám đốc tài chính'))
    director_id = fields.Many2one('hr.employee', string='Giám đốc', default=lambda self: self._get_role('Giám đốc'))

    # Thông tin lương
    adjust_type = fields.Selection([('increase','Tăng lương'),('decrease','Giảm lương')], string='Loại điều chỉnh', required=True)
    date_start = fields.Date(string='Ngày bắt đầu', required=True, default=lambda self: date.today())
    reason = fields.Text(string='Lý do')

    # Thông tin lương cũ và mới
    old_salary_social = fields.Char(string='Lương đóng BHXH cũ', readonly=True)
    old_salary_type = fields.Selection([('monthly','Theo tháng'),('hourly','Theo giờ'),('coefficient','Theo hệ số')], string='Loại lương cũ', readonly=True)
    old_salary_negotiated = fields.Float(string='Lương thỏa thuận cũ', readonly=True)
    old_salary_base = fields.Float(string='Lương cơ bản cũ', readonly=True)
    old_salary_kpi = fields.Float(string='Lương KPI cũ', readonly=True)
    old_salary_structure = fields.Char(string='Cấu trúc lương cũ', readonly=True)

    new_salary_social = fields.Float(string='Lương đóng BHXH mới')
    new_salary_type = fields.Selection([('monthly','Theo tháng'),('hourly','Theo giờ'),('coefficient','Theo hệ số')], string='Loại lương mới')
    new_salary_negotiated = fields.Float(string='Lương thỏa thuận mới')
    new_salary_base = fields.Float(string='Lương cơ bản mới')
    new_salary_kpi = fields.Float(string='Lương KPI mới')
    new_salary_structure = fields.Selection([('CBNV 2025','CBNV 2025'),('probation85','Thử việc - 85% lương'),('other','Khác')], string='Cấu trúc lương mới')

    # Phụ cấp
    allowance_ids = fields.One2many('dcl.allowance', 'dcl_id', string='Phụ cấp')

    # Mã quyết định
    code = fields.Char(string='Mã quyết định', readonly=True)

    @api.onchange('employee_id')
    def _onchange_employee(self):
        for rec in self:
            hr = rec.employee_id
            contract = hr.contract_id
            # Lấy CMND/Hộ chiếu thay vì ssn
            rec.old_salary_social = hr.identification_id or ''
            rec.old_salary_type = contract.wage_type if contract else False
            rec.old_salary_negotiated = contract.wage if contract else 0.0
            rec.old_salary_base = contract.basic_wage if contract else 0.0
            rec.old_salary_kpi = contract.kpi_wage if contract else 0.0
            rec.old_salary_structure = contract.labor_structure if contract else False
            # load allowances
            rec.allowance_ids = [(5,)]
            for al in getattr(hr, 'allowance_ids', []):
                rec.allowance_ids += (0,0,{
                    'allowance_type': al.code,
                    'old_amount': al.amount,
                    'old_unit': al.unit,
                })

    @api.model
    def _get_role(self, title):
        employee = self.env['hr.employee'].search([('job_title','=',title)], limit=1)
        return employee.id or False

    # Actions
    def action_send_hcns(self):
        self.state = 'waiting_hcns'

    def action_approve(self):
        self.state = 'done'

    def action_reject(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'dcl.reject.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_dcl_id': self.id}
        }

    def action_cancel(self):
        self.state = 'cancelled'

    def action_back_to_draft(self):
        self.state = 'draft'