# -*- coding: utf-8 -*-
{
    'name': "Quản lý nhân viên",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    'assets': {
        'web.assets_backend': [
            'qlnv/static/src/scss/*.scss',
            'qlnv/static/src/scss/style.scss',
        ],
    },
    
    'data': [
        'demo/demo.xml',
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/department_view.xml',
        'views/information_employee.xml',
        'views/employee_root_menu.xml',
        'views/departure_reason_view.xml',
        'views/job_position_view.xml',
        'views/contract_type_view.xml',
        'views/medal_view.xml',
        'views/config_ip_view.xml',
        'views/cv.face_recognition_view.xml',
    ],
    
    
    'application': True,
    
}

