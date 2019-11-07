# -*- coding: utf-8 -*-
{
    'name': '	Egyptian Growers Partner Enhancement',
    'version': '1.0',
    'category': 'base',
    'author': 'Zadsolutions, Ahmed Hussein',
    'website': "http://zadsolutions.com",
    'summary': """
    Egyptian Growers Partner
    """,
    'depends': ['base','account_reports'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}