{
    'name': 'HR Job Extension',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Mở rộng chức năng Chức vụ của module Bộ Máy Tổ Chức',
    'description': """Mô-đun mở rộng để quản lý thông tin Chức vụ, bao gồm phụ cấp và thông tin tuyển dụng.""",
    'author': 'Dang Thai Minh Vu',
    'license': 'LGPL-3',
    'depends': ['base', 'hr', 'hr_contract','mail'],
    'assets': {
        'web.assets_backend': [
            'bo_may_to_chuc_hr_job/static/lib/tiptap/tiptap.umd.js',
            'bo_may_to_chuc_hr_job/static/lib/tiptap/slash-menu.umd.js',
            'bo_may_to_chuc_hr_job/static/src/js/slash_text_widget.js',
            'bo_may_to_chuc_hr_job/static/src/css/custom_tabs.css'
        ],
    },
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hr_job_custom_views.xml',
        'views/res_company_location_line_popup.xml',
        'views/res_company_custom_views.xml',
        'views/hr_department_custom_views.xml',
        'views/hr_employee_views.xml',
        'views/x_contract_appendix_views.xml'
        ],
    'installable': True,
    'application': False,
}
