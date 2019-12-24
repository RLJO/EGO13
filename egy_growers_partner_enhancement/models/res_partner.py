# -*- coding: utf-8 -*-

from odoo import models, fields, api,_,tools, SUPERUSER_ID
from odoo.tools import pycompat
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class EgyGrowersResPartner(models.Model):
    _inherit = 'res.partner'

    other_mobiles = fields.Many2many('res.partner.mobiles',string='Other Mobiles')
    fax = fields.Many2many('res.partner.fax',string='Fax')
    supplier_country = fields.Many2many('res.country',string='Supplier Country')
    partner_company_type = fields.Selection(string='Company Type',selection=[('wholesale','Wholesale'),
                                                                     ('retail','Retail'),
                                                                     ('reseller','Reseller'),
                                                                     ('partner','Partner')])
    other_emails = fields.Many2many('res.partner.emails',string='Email 2')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    #
    @api.onchange('first_name','last_name')
    def onchange_first_last_name(self):
        first_name = self.first_name if self.first_name else ''
        last_name = self.last_name if self.last_name else ''
        if first_name or last_name:
            self.name = first_name + ' ' + last_name

    def open_proforma_partner_ledger(self):
        return {
            'type': 'ir.actions.client',
            'name': _('Proforma Partner Ledger'),
            'tag': 'account_report',
            'options': {'partner_ids': [self.id]},
            'ignore_session': 'both',
            'context': "{'model':'account.proforma.partner.ledger'}"
        }

class EgyGrowersPartnerOtherMobiles(models.Model):
    _name = 'res.partner.mobiles'
    _rec_name = 'name'
    _order = 'name'
    _description = 'Partner Mobiles'

    name = fields.Char()


class EgyGrowersPartnerFaxTypes(models.Model):
    _name = 'res.partner.fax'
    _rec_name = 'name'
    _order = 'name'
    _description = 'Partner Fax'

    name = fields.Char()

class EgyGrowersPartnerOtherEmails(models.Model):
    _name = 'res.partner.emails'
    _rec_name = 'name'
    _order = 'name'
    _description = 'Partner Emails'

    name = fields.Char()
