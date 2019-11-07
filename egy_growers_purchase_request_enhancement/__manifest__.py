# -*- coding: utf-8 -*-
{
    'name': '	Egyptian Growers Purchase Request Enhancement',
    'version': '1.0',
    'category': 'purchase',
    'author': 'Zadsolutions, Ahmed Hussein',
    'website': "http://zadsolutions.com",
    'summary': """
    Egyptian Growers Purchase Request
    """,
    'depends': ['base','sprogroup_purchase_request'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_request.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}