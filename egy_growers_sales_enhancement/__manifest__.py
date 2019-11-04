# -*- coding: utf-8 -*-
{
    'name': '	Egyptian Growers Sales Enhancement',
    'version': '1.0',
    'category': 'sale',
    'author': 'Zadsolutions, Ahmed Hussein',
    'website': "http://zadsolutions.com",
    'summary': """
    Egyptian Growers Sales
    """,
    'depends': ['base','sale','sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/sale_order_report.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
