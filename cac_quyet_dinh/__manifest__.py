{
    'name': 'Các Quyết Định',
    'version': '1.0',
    'summary': 'Quản lý các quyết định như khen thưởng, kỷ luật, bổ nhiệm,...',
    'description': """
        Module quản lý các quyết định trong doanh nghiệp, bắt đầu với tính năng Khen thưởng.
    """,
    'category': 'Human Resources',
    'author': 'Ban Tu',
    'depends': ['base', 'hr', 'mail', 'hr_contract', 'bo_may_to_chuc_hr_job'],
    'data': [
        'data/sequence.xml',
        'views/khen_thuong_views.xml',
        'views/khen_thuong_wizard_views.xml',
        'views/ky_luat_views.xml',
        'views/ky_luat_wizard_views.xml',
        'views/dieu_chinh_luong_views.xml',
        'views/dieu_chinh_luong_wizard_views.xml',
        'views/transfer_work_views.xml',
        'views/appoint_views.xml',
        'views/menu_views.xml',
        'security/cac_quyet_dinh_security.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
