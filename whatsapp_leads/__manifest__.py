# -*- coding: utf-8 -*-

{
    'name': 'Send Whatsapp Message',
    'version': '13.0.1.0.0',
    'summary': 'Send Message to Lead via Whatsapp web',
    'description': 'Send Message to Lead via Whatsapp web',
    'category': 'Extra Tools',
    'author': 'melbadry@white-code.co.uk',
    'company': 'white Code',
    'website': 'white-code.co.uk',
    'depends': [
        'base','crm'
        ],
    'data': [
        'views/view.xml',
        'wizard/wizard.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
