{
    'name': 'Các Quyết Định',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Mở rộng chức năng Chức vụ của module Bộ Máy Tổ Chức',
    'description': """Mô-đun mở rộng để quản lý thông tin Chức vụ, bao gồm phụ cấp và thông tin tuyển dụng.""",
    'author': 'Dang Thai Minh Vu',
    'license': 'LGPL-3',
    'depends': ['base', 'hr','mail'],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        ],
    'installable': True,
    'application': False,
}
