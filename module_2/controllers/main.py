# -*- coding: utf-8 -*-
import json
from urllib import request
from odoo import http # type: ignore


class Module2(http.Controller):
    @http.route('/module_2/module_2', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/module_2/module_2/objects', auth='public')
    def list(self, **kw):
        return http.request.render('module_2.listing', {
            'root': '/module_2/module_2',
            'objects': http.request.env['player'].search([]),
        })

    @http.route('/module_2/module_2/objects/<model("player"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('module_2.object', {
            'object': obj
        })
        
    # @http.route('/module_2/module_2', auth='public', type='http')
    # def mountain_check(self):
    #     return "module_2/module_2 check check check"

    # @http.route('/module_2/module_2/<int:id>', auth='public', type='http')
    # def mountain_check(self, id):
    #     return "module_2/module_2 check check check %s" % str(id)

    # @http.route('/module_2/module_2', auth='public')
    # def mountain_check(self):
    #     return werkzeug.utils.redirect('https://www.google.com')

    # @http.route('/module_2/module_2', auth='public')
    # def mountain_check(self):
    #     return request.render('web.login')

    # @http.route('/module_2/module_2', auth='public', type='http')
    # def mountain_check(self):
    #     return json.dumps({
    #         "check": "check 123"
    #     })

    # @http.route('/module_2/module_2', auth='public', type='http')
    # def mountain_check(self):
    #     partner = request.env['res.partner'].sudo().create({
    #         'name': 'module_2/module_2'
    #     })
    #     return 'Partner has been created'


