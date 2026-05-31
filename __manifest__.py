{
    'name': 'HR Custom',
    'version': '1.0',
    'author': 'Oussema Mhamed',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/hr_department_views.xml',
    ],
    'installable': True,
    'application': True,
}