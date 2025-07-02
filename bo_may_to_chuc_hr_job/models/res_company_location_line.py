from odoo import models, fields, api

class ResCompanyLocationLine(models.Model):
    _name = 'res.company.location.line'
    _description = 'Dòng thông tin địa điểm'

    company_id = fields.Many2one(
        'res.company.custom', ondelete='cascade', index=True,
        string='Công ty', required=True
    )

    location_name = fields.Char(string='Tên địa điểm', required=True)
    location_short_name = fields.Char(string='Tên viết tắt') 
    location_is_headquarter = fields.Boolean(string='Trụ sở chính', default=False)

    location_country_id = fields.Many2one('res.country', string='Quốc gia')
    location_state_id = fields.Many2one('res.country.state', string='Tỉnh/Thành phố', domain="[('country_id','=', location_country_id)]")
    location_district_id = fields.Many2one('res.country.district', string='Quận/Huyện', domain="[('state_id','=', location_state_id)]")
    location_street_id = fields.Many2one('res.country.street', string='Đường', domain="[('district_id','=', location_district_id)]")
    location_address = fields.Char(string='Địa chỉ chi tiết')

    location_phone = fields.Char(string="Điện thoại")
    location_email = fields.Char(string="Email")

    @api.onchange('location_is_headquarter')
    def _onchange_headquarter(self):
        if self.location_is_headquarter:
            for line in self.company_id.location_line_ids:
                if line != self:
                    line.location_is_headquarter = False
