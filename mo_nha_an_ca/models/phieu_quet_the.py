from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PhieuQuetThe(models.Model):
    _name = 'mo_nha_an_ca.phieu_quet_the'
    _description = 'Phieu quet the an ca'

    employee_id = fields.Many2one('hr.employee', string='CBCNV', required=True)
    ngay = fields.Datetime(string='Thoi gian quet', required=True, default=fields.Datetime.now)
    ca = fields.Selection([
        ('ca1', 'Ca 1'),
        ('ca2', 'Ca 2'),
        ('ca3', 'Ca 3')], string='Ca', required=True)
    vi_tri = fields.Char(string='Vi tri quet', required=True)
    trang_thai = fields.Selection([
        ('hop_le', 'Hop le'),
        ('khong_hop_le', 'Khong hop le')], string='Trang thai', readonly=True, default='khong_hop_le')

    @api.model
    def quet_the(self, employee_id, vi_tri):
        """
        Xu ly qua trinh quet the.
        """
        employee = self.env['hr.employee'].browse(employee_id)
        if not employee:
            raise ValidationError(_("Khong tim thay CBCNV."))

        # Kiem tra hop le
        if self._kiem_tra_hop_le(employee):
            self.create({
                'employee_id': employee.id,
                'vi_tri': vi_tri,
                'ca': self._xac_dinh_ca(),
                'trang_thai': 'hop_le',
            })
            self._mo_cua()
        else:
            self.create({
                'employee_id': employee.id,
                'vi_tri': vi_tri,
                'ca': self._xac_dinh_ca(),
                'trang_thai': 'khong_hop_le',
            })
            self._khong_mo_cua()

    def _kiem_tra_hop_le(self, employee):
        """
        Kiem tra xem CBCNV co hop le de vao nha an hay khong.
        """
        # Logic kiem tra hop le
        return True  # Placeholder: Gia su tat ca hop le

    def _xac_dinh_ca(self):
        """
        Xac dinh ca hien tai dua tren thoi gian.
        """
        current_hour = fields.Datetime.now().hour
        if 6 <= current_hour < 12:
            return 'ca1'
        elif 12 <= current_hour < 18:
            return 'ca2'
        elif 18 <= current_hour <= 23:
            return 'ca3'
        else:
            return 'ca1'  # Mac dinh la Ca 1 neu ngoai gio

    def _mo_cua(self):
        """
        Mo cua cho CBCNV vao nha an.
        """
        # Tich hop voi he thong mo cua
        pass

    def _khong_mo_cua(self):
        """
        Khong mo cua neu khong hop le.
        """
        # Xu ly khi khong hop le
        pass

    def bam_nut_mo_cua_ra(self):
        """
        Xu ly bam nut mo cua de ra khoi nha an.
        """
        # Logic mo cua ra
        pass