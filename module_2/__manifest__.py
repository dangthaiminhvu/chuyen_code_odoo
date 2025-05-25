# -*- coding: utf-8 -*-
{
    'name': "module_2",
    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Dangthaiminhvu", # ten tac gia
    'website': "https://www.yourcompany.com", # website cua minh, co thi them vao, khong co thi thoi

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    #noi lay du lieu
    'data': [
        'security/player_security.xml',
        'security/ir.model.access.csv',
        'views/player_views.xml',
    ],

    # Muon mudule_2 hoat dong thi can phai cai nhung cai trong depend
    'depends': ['base', 'website'],

    'assets': {
        'web.assets_frontend': [
            'module_2/css/styles.css',  # Đường dẫn tới tệp CSS của bạn
        ],
    },
}

