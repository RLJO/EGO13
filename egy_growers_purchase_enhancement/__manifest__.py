# -*- coding: utf-8 -*-
{
    'name': '	Egyptian Growers Purchase Enhancement',
    'version': '1.0',
    'category': 'purchase',
    'author': 'Zadsolutions, Ahmed Hussein',
    'website': "http://zadsolutions.com",
    'summary': """
    Egyptian Growers Purchase
    """,
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/purchase_order.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}