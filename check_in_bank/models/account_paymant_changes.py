# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import Warning

## Ahmed Salama Code Start ---->
class AccountPayment(models.Model):
	_inherit = 'account.payment'
	
	def create_check(self, check_type, operation, bank):
		self.ensure_one()
		check_vals = {
			'bank_id': bank.id,
			'owner_name': self.check_owner_name,
			'owner_vat': self.check_owner_vat,
			'number': self.check_number,
			'name': self.check_name,
			'checkbook_id': self.checkbook_id.id,
			'issue_date': self.check_issue_date,
			'type': self.check_type,
			'journal_id': self.journal_id.id,
			'amount': self.amount,
			'payment_date': self.check_payment_date,
			'partner_id': self.partner_id.id,
			# TODO arreglar que monto va de amount y cual de amount currency
			# 'amount_currency': self.amount,
			'currency_id': self.currency_id.id,
		}
		check = self.env['account.check'].create(check_vals)
		self.check_ids = [(4, check.id, False)]
		check._add_operation(
			operation, self, self.partner_id, date=self.payment_date)
		return check

## Ahmed Salama Code End.
