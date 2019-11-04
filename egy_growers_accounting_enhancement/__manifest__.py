# -*- coding: utf-8 -*-
{
    'name': '	Egyptian Growers Accounting Enhancement',
    'version': '1.0',
    'category': 'account',
    'author': 'Zadsolutions, Ahmed Hussein',
    'website': "http://zadsolutions.com",
    'summary': """
    Egyptian Growers Accounting
    """,
    'depends': ['base','account','sale','egy_growers_purchase_enhancement','egy_growers_sales_enhancement','account_check'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/account_invoice.xml',
        'views/account_invoice_refund.xml',
        'views/account_payment.xml',
        'views/vendor_bill.xml',
        'views/account_bank_statement.xml',
        'views/templates.xml',
        'reports/account_invoice_report_changes.xml',
        'reports/journal_audit_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}