{
    'name': 'ngay_nghi',
    'version': '1.0',
    'summary': 'Quản lý ngày nghỉ của nhân viên',
    'description': 'Module quản lý ngày nghỉ, nghỉ phép, nghỉ chế độ, nghỉ thai sản,...',
    'author': 'Your Company',
    'depends': [
        'base',
        'hr',
        'bo_may_to_chuc_hr_job',
        'hr_holidays',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/leave_request_sequence.xml',
        'views/leave_request_views.xml',
        'views/leave_summary_views.xml',
        'views/leave_allocation_views.xml',
        'views/hr_leave_type_views.xml',
        'views/holiday_calendar_line_views.xml',
        'views/leave_request_menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}