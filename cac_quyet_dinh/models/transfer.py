from odoo import api, fields, models, _

class CacQuyetDinhTransfer(models.Model):
    _name = 'cac.quyetdinh.renew.contract'
    _description = 'Tái ký / Gia hạn hợp đồng'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Mã quyết định', readonly=True, copy=False, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True, tracking=True)
    job_id = fields.Many2one('hr.job.custom', string='Chức vụ', readonly=True)
    department_id = fields.Many2one('hr.department', string='Phòng/Ban', readonly=True)

    manager_id = fields.Many2one('hr.employee', string='Cán bộ quản lý', required=True)
    manager_job_id = fields.Many2one('hr.job.custom', string='Chức vụ CBQL', readonly=True)

    # Ý kiến nhân viên
    strengths_emp    = fields.Text(string='Điểm mạnh')
    weaknesses_emp   = fields.Text(string='Điểm yếu')
    employee_comment = fields.Text(string='Ý kiến của nhân viên')

    # Ý kiến quản lý
    strengths_mgr    = fields.Text(string='Điểm mạnh')
    weaknesses_mgr   = fields.Text(string='Điểm yếu')
    manager_comment  = fields.Text(string='Ý kiến của quản lý', readonly=True)

    # Lương cũ
    salary_type     = fields.Selection([('month','Tháng'),('hour','Giờ')], string='Kiểu lương', readonly=True)
    old_wage        = fields.Monetary(string='Mức lương cũ', currency_field='company_currency', readonly=True)
    structure_type  = fields.Selection([('type1','Cấu trúc A'),('type2','Cấu trúc B')], string='Cấu trúc lương', readonly=True)

    # Lương mới
    salary_type_new    = fields.Selection([('month','Tháng'),('hour','Giờ')], string='Kiểu lương mới')
    new_wage           = fields.Monetary(string='Mức lương mới', currency_field='company_currency')
    contract_info      = fields.Char(string='Thông tin HĐ mới')
    structure_type_new = fields.Selection([('type1','Cấu trúc A'),('type2','Cấu trúc B')], string='Cấu trúc lương mới')

    contract_type = fields.Selection([('new', 'Hợp đồng ký mới'), ('renew','Tái ký/ Gia hạn')], string='Kiểu hợp đồng')
    
    new_contract_file = fields.Binary(string="File hợp đồng mới", readonly=True)
    
    approve_hrm_id = fields.Many2one('hr.employee', string='TP.HCNS')
    approve_ceo_id = fields.Many2one('hr.employee', string='Giám đốc')
    responsible_id = fields.Many2one('hr.employee',string='Người chịu trách nhiệm')
    general_evaluation = fields.Text(string='Lý do')    
    official_contract = fields.Text(string='HĐ chính thức', readonly=True)
    confirmed_salary = fields.Float(string='Lương xác nhận')
    start_date = fields.Date(string='Ngày bắt đầu')
    end_date = fields.Date(string='Ngày kết thúc')
    manager_proposal = fields.Text(string='Đề xuất của CBQL')
    is_employee = fields.Boolean(string='Is Employee')
    is_manager = fields.Boolean(string='Is Manager')
    new_salary_month = fields.Char(string='Tháng lương mới')
    note = fields.Text(string="Ghi chú")

    # Quan hệ
    line_ids           = fields.One2many('cac.quyetdinh.transfer.line', 'transfer_id', string='Đánh giá chi tiết')
    challenge_ids      = fields.One2many('cac.quyetdinh.challenge', 'transfer_id', string='Thử thách')

    state = fields.Selection([
        ('draft', 'Bản nháp'),
        ('to_manager', 'Chờ CBQL phê duyệt'),
        ('rejected', 'Bị từ chối'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Hủy'),
    ], string='Trạng thái', default='draft', tracking=True)

    company_currency = fields.Many2one('res.currency', related='employee_id.company_id.currency_id', readonly=True)
    
    total_score = fields.Float(string='Tổng điểm đánh giá', compute='_compute_total_score', store=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cac.quyetdinh.renew.contract')
        return super().create(vals)
    
    @api.onchange('manager_id')
    def _onchange_manager(self):
        if self.manager_id:
            self.manager_job_id = self.manager_id.job_id

    def _get_hcns(self):
        return self.env['hr.employee'].search([('job_id','ilike','HCNS')], limit=1)

    def _get_director(self):
        return self.env['hr.employee'].search([('job_id','ilike','Giám đốc')], limit=1)

    @api.depends('line_ids.score')
    def _compute_total_score(self):
        for rec in self:
            rec.total_score = sum(rec.line_ids.mapped('score'))

    def action_send_to_manager(self):
        self.state = 'to_manager'
        # gửi notification, email, activity ..

    def action_reject(self):
        self.state = 'rejected'

    def action_cancel(self):
        self.state = 'cancel'

    def action_done(self):
        self.state = 'done'

    @api.onchange('employee_id')
    def _onchange_employee(self):
        if self.employee_id:
            self.job_id = self.employee_id.job_id
            self.department_id = self.employee_id.department_id
            cn = self.employee_id.contract_id
            if cn:
                self.salary_type = getattr(cn, 'wage_type', False)  # nếu có custom
                self.old_wage = cn.wage
                self.structure_type = getattr(cn, 'structure_type', False)
            else:
                self.salary_type = False
                self.old_wage = 0.0
                self.structure_type = False

