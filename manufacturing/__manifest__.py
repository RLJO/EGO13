# -*- coding: utf-8 -*-
{
    'name' : 'Manufacturing Custom',
    'version' : '1.0',
    'category': '',
    'description': """
   

    """,
    'depends' : ['base','mrp','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/manufaturing_custom.xml',
        'views/bom_custom.xml',
        'views/manufacturing_wizard_view.xml',
        'views/manufacturing_report_template.xml',



    ],
    'installable': True,
    'application': True,
}