# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Zad Cheque In Bank (Bank check)',
    'version': '10.0.0.1',
    'category': 'Accounting',
    'description': """
This module is used to enhance Account Cheque module .
==============================================
    * Add new state/operation [In Bank] to create this state journals.
    * Add new action to return third check with selected partner.
    * Change accounts that created from Debited action.

""",
    'author': 'zadsolutions, Ahmed Salama',
    'website': 'https://www.zadsolutions.com',
    'depends': ['stock','account','account_accountant','account_check'],
    'data': [
        'view/account_check_changes.xml',
        'view/res_company_view.xml',
        'wizard/check_action_view_changes.xml',
    ],
    'demo': [],
    'test': [],
    'images': ['static/description/main.png'],
    
    'installable': True,
    'auto_install': False,
    'price': 34.99,
    'currency': 'EUR',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
