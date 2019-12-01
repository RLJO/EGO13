# -*- coding: utf-8 -*-
{
    'name' : 'Planning Module',
    'version' : '1.0',
    'category': '',
    'description': """
   

    """,
    'depends' : ['base'],
    'data': [
        'security/security_groups_view.xml',
        'security/ir.model.access.csv',
        'views/planning_views.xml',
        'views/planning_second_views.xml',
        'views/planning_third_views.xml',

    ],
    'installable': True,
    'application': True,
}