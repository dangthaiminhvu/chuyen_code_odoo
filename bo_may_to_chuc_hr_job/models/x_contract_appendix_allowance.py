from odoo import models, fields

class ContractAppendixAllowance(models.Model):
    _name = 'x.contract.appendix.allowance'
    _description = 'Allowance Line in Contract Appendix'

    appendix_id = fields.Many2one('x.contract.appendix', string='Phụ lục', required=True, ondelete='cascade')
    name = fields.Char(string='Phụ cấp', required=True)
    amount = fields.Float(string='Mức hưởng', required=True)
    unit = fields.Char(string='Đơn vị', default='VND')
