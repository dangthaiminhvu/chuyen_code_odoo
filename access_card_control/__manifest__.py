{
    'name': "access_card_control",
    
    'web_icon': 'access_card_control/static/description/icon.png',


    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dang Thai Minh Vu",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'data': [
        'security/access_card_security.xml',
        'security/ir.model.access.csv', 
        'views/access_card_views.xml',
    ],
    
    'depends': ['base'],
}