# -*- coding: utf-8 -*-
{
    'name' : 'QC Reports',
    'version' : '1.0',
    'category': '',
    'description': """
   

    """,
    'depends' : ['base','mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/manufaturing_custom.xml',
        # 'views/qc_packing_stock.xml',

        'views/qc_packing_wizard_view.xml',
        'views/qc_packing_report_template.xml',
        'views/res_partner_custom.xml',
        'views/qc_farm_wizard_view.xml',
        'views/qc_farm_report_template.xml',



    ],
    'installable': True,
    'application': True,
}