{
    'name': "mo_nha_an_ca",
    
    'web_icon': 'access_card_control/static/description/icon.png',


    'summary': """  
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
Phân hệ Nhà ăn ca:
1. Thiết lập định mức ăn công nghiệp
2. Đăng ký vị trí ăn
3. Đăng ký suất ăn
4. Báo ăn
5. Chấm ăn (cả tự động qua quẹt thẻ và nhập tay khi ngoại lệ)
6. Theo dõi quẹt thẻ
7. Báo cáo thống kê
    """,

    'author': "Dang Thai Minh Vu",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'data': [
        'security/mo_nha_an_ca_security.xml',
        'security/ir.model.access.csv',
        'views/mo_nha_an_ca_views.xml',
        'views/dinh_muc_an_views.xml',
        'views/dang_ky_vi_tri_views.xml',
        'views/dang_ky_suat_an_views.xml',
        'views/bao_an_views.xml',
        'views/cham_an_views.xml',
        'views/phieu_quet_the_views.xml',
        'views/an_ca_views.xml',
    ],
    
    'depends': ['base', 'hr'],
}