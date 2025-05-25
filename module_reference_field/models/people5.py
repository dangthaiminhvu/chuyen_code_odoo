from odoo import models, fields # type: ignore

class People(models.Model):
    _name = 'people5'
    _description = 'People5'

    def _selection_list(self):
        return [(model.model, model.name) for model in self.env['ir.model'].search([])] #dang tim kiem tat ca cac ban ghi trong ir.model
    #ir.model la noi luu tru tat ca model ma ta da tao ra tu truoc den gio trong CSDL

    name = fields.Char(string='Name')

    # Reference field
    reference = fields.Reference(selection=_selection_list, string='Reference')

    # Many2oneReference field
    res_model = fields.Char('Model Name', required=True, index=True)
    m2o_reference = fields.Many2oneReference(model_field='res_model', string='Many2oneReference')