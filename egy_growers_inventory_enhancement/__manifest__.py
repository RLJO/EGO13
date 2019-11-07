# -*- coding: utf-8 -*-
{
    'name': '	Egyptian Growers Inventory Enhancement',
    'version': '1.0',
    'category': 'stock',
    'author': 'Zadsolutions, Ahmed Hussein',
    'website': "http://zadsolutions.com",
    'summary': """
    Egyptian Growers Inventory
    """,
    'depends': ['base','stock','sale','account','egy_growers_sales_enhancement',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/logistics_report_wiz_views.xml',

        'reports/reports.xml',
        'reports/packing_list_report_view.xml',

        'views/stock_picking.xml',
        'views/product_template_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
