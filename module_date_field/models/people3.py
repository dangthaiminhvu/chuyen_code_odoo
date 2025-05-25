from odoo import models, fields # type: ignore


class People3(models.Model):
    _name = 'people3'
    _description = 'People3'

    name = fields.Char(string='Name')

    # Date field
    date = fields.Date(string='Date')

    # Date time field
    datetime = fields.Datetime(string='Date time')

    def action_check(self):
        pass #pass la lenh khong lam gi ca, ham khong the khai bao ma khong lam gi nhung lenh nay se giup cho ham khong loi.