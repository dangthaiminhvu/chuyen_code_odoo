from odoo import models, fields # type: ignore


class House(models.Model):
    _name = 'house'
    _description = 'House'

    name = fields.Char(string='Name')

    # Many2one field
    people4_id = fields.Many2one('people4', string='Owner')
    
    # people4_id = fields.Many2one('people4', string='Owner', domain[{'name','=','Người thứ 1'}]) 
    # cái này dùng khi muốn chỉ có Người thứ 1 hiện lên khi chọn house (chi co khi nao name = Nguoi thu 1)
    
    # people4_id = fields.Many2one('people4', string='Owner', ondelete='restrict')
    # Cái này dùng khi không cho người nào xóa dữ liệu này di (co cac lua chon ondelete la 'set null', 'restrict', 'cascade')

    # Many2many field
    people4_ids = fields.Many2many('people4', string='People4')