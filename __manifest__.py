{
    'name': 'Custom Auth and Dashboard',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom login, registration, and Grafana dashboard integration',
    'description': 'Custom Authentication and Dashboard Integration',
    'depends': ['base', 'web'],
    'data': [
        'views/auth.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
