{
    'name': 'Quản Lý Nhân Sự',
    'version': '1.0',
    'category': 'Nhân Sự',
    'summary': 'Quản lý thông tin nhân sự cho mỏ',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/nhan_su_views.xml',
        'views/ca_lam_viec_views.xml',
    ],
    'installable': True,
    'application': False,
}