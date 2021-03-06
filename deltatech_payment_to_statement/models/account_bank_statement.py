# -*- coding: utf-8 -*-
# ©  2018 Deltatech
# See README.rst file on addons root folder for license details


from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    @api.model
    def create(self, vals):
        if 'name' not in vals or vals['name'] in ['/', '', False]:
            journal = self.env['account.journal'].browse(vals['journal_id'])
            if journal.statement_sequence_id:
                vals['name'] = journal.statement_sequence_id.next_by_id()
        return super(AccountBankStatement, self).create(vals)


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    payment_id = fields.Many2one('account.payment')
