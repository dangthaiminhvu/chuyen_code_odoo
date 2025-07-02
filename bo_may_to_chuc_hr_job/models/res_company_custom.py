from odoo import models, fields, api

class ResCompanyCustom(models.Model):
    _name = 'res.company.custom'
    _description = 'Thông tin công ty mở rộng'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # 1.1 Tên công ty
    name = fields.Char(string='Tên công ty', required=True, tracking=True)

    # 1.2 Thông tin công ty chung
    logo = fields.Image(string='Logo công ty')
    identifier_type = fields.Selection([
        ('tax', 'Mã số thuế'),
        ('social', 'Mã số BHXH'),
        ('cid', 'Citizen Identity Card'),
        ('id', 'Identity Card'),
        ('other', 'Khác')
    ], string='Loại định danh')
    identifier_code = fields.Char(string='Mã định danh')
    short_name = fields.Char(string='Tên viết tắt')
    website = fields.Char(string='Website')
    tax_code = fields.Char(string='Mã số thuế')
    phone = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    favicon = fields.Image(string='Favicon công ty')

    # 1.3 Văn phòng giao dịch
    trading_office_country_id = fields.Many2one(
        'res.country', string='Quốc gia Văn phòng',
    )
    trading_office_state_id = fields.Many2one(
        'res.country.state', string='Tỉnh/Thành phố Văn phòng',
        domain="[('country_id','=', trading_office_country_id)]"
    )
    trading_office_district_id = fields.Many2one(
        'res.country.district', string='Quận/Huyện Văn phòng',
        domain="[('state_id','=', trading_office_state_id)]"
    )

    trading_office_street_id = fields.Many2one(
        'res.country.street', string='Đường Văn phòng',
        domain="[('district_id','=', trading_office_district_id)]"
    )
    trading_office_address = fields.Char(string='Địa chỉ chi tiết Văn phòng')

    # 1.4 Trụ sở chính
    headquarters_country_id = fields.Many2one(
        'res.country', string='Quốc gia Trụ sở',
    )
    headquarters_state_id = fields.Many2one(
        'res.country.state', string='Tỉnh/Thành phố Trụ sở',
        domain="[('country_id','=', headquarters_country_id)]"
    )
    headquarters_district_id = fields.Many2one(        
        'res.country.district', string='Quận/Huyện Trụ sở',
        domain="[('state_id','=', headquarters_state_id)]")
    headquarters_street_id = fields.Many2one(
        'res.country.street', string='Đường Trụ sở',
        domain="[('district_id','=', headquarters_district)]")
    headquarters_address = fields.Char(string='Địa chỉ chi tiết Trụ sở')

    # 1.5 Thông tin người đại diện
    representative_name = fields.Char(string='Người đại diện')
    representative_position = fields.Char(string='Chức vụ')
    representative_email = fields.Char(string='Email người đại diện')
    representative_phone = fields.Char(string='SĐT người đại diện')

    # 1.6 Địa điểm (One2many)
    location_line_ids = fields.One2many(
        'res.company.location.line', 
        'company_id',
        string='Địa điểm công ty'
    )


    # 1.7 Bảo hiểm (One2many)
    insurance_line_ids = fields.One2many(
        'res.company.insurance.line', 
        'company_id', 
        string='Thông tin bảo hiểm'
    )

    # 1.8 Đơn vị (UNIT)
    unit_code = fields.Char(string='Mã đơn vị')
    unit_province_id = fields.Many2one('res.country.state', string='Tỉnh/Thành phố')
    unit_representative_id = fields.Many2one('res.partner', string='Người đại diện')
    unit_representative_position = fields.Char(string='Chức vụ người đại diện')
    payment_method = fields.Selection([
        ('monthly', 'Hàng tháng'),
        ('quarterly', 'Hàng quý'),
        ('yearly', 'Hàng năm')
    ], string='Phương thức đóng')
    receive_result = fields.Selection([
        ('office', 'Nhận tại cơ quan bảo hiểm'),
        ('post', 'Nhận qua bưu điện')
    ], string='Đăng ký nhận kết quả')

    # 1.9 Liên hệ
    contact_type = fields.Selection([
        ('app', 'App/Website'),
        ('admin', 'Administrator'),
        ('test2', 'Công ty TEST 2'),
        ('other', 'Khác')
    ], string='Loại liên hệ')
    contact_phone = fields.Char(string='SĐT liên hệ')
    contact_email = fields.Char(string='Email liên hệ')

    # 1.10 Thông tin ngân hàng
    bank_name = fields.Char(string='Ngân hàng')
    bank_branch = fields.Char(string='Chi nhánh')
    bank_account = fields.Char(string='Tài khoản ngân hàng')