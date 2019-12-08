# -*- coding: utf-8 -*-
{
    'name' : 'LOGISTIC',
    'version' : '1.0',
    'category': '',
    'description': """
   

    """,
    'depends' : ['base','stock'],
    'data': [
        'security/security_groups_view.xml',
        'security/ir.model.access.csv',
        'views/logistic_views.xml',
        'views/car_types_view.xml',
        'views/supplier_view.xml',
        'views/stock_picking_custom.xml',
        'views/logistic_report_wizard_view.xml',
        'views/logistic_report_template.xml',


    ],
    'installable': True,
    'application': True,
}