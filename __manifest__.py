{
    'name': "University",

    'summary': "University Management System",
    'author': "Lisandro Romero",
    'website': "https://lisandro-romero.vercel.app/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/professor_views.xml',
        'views/career_views.xml',
        'views/study_plan_views.xml',
        'views/subject_views.xml',
        'views/enrollment_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

