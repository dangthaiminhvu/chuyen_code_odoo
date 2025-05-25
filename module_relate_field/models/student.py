from odoo import models, fields, api # type: ignore


class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    people7_id = fields.Many2one('people7', string='People7')
    name = fields.Char(related='people7_id.name', store=True)