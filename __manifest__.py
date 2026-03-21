{
    'name': 'Odoo Gfis Module',
    'version': '1.0',
    'summary': 'Custom Sale Order Fields',
    'depends': ['sale', 'hr'],
    'data': [
        'views/sale_order_views.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
    'application': False,
}