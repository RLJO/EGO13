# -*- coding: utf-8 -*-
{
    'name' : 'EGO SALES AND purchase customs',
    'version' : '1.0',
    'category': '',
    'description': """
   

    """,
    'depends' : ['base','account','sale','purchase','hr','mail'],
    'data': [
        'security/security_groups_view.xml',
        'security/purchase_request_security.xml',
        'security/sales_security.xml',
        'security/ir.model.access.csv',

        'views/account_move.xml',
        'views/sale_order_custom.xml',
        'views/contract_view.xml',
        'views/purchase_requets_view.xml',
        'views/purchase_request_data.xml',



        # 'views/purchase_order_custom.xml',

    ],
    'installable': True,
    'application': True,
}