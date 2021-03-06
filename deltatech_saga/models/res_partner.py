# -*- coding: utf-8 -*-
# ©  2017 Deltatech
# See README.rst file on addons root folder for license details


from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
import math

 

class res_partner(models.Model):
    _inherit = "res.partner" 

    ref_customer = fields.Char(string="Code Customer SAGA", size=5)
    ref_supplier = fields.Char(string="Code Supplier SAGA", size=5)


    @api.model
    def create(self,   vals ):  
        if ('ref_customer' not in vals) or (vals.get('ref_customer') in ('/', False)):
            if  vals.get('customer',False): 
                sequence = self.env.ref('deltatech_saga.sequence_ref_customer')
                if sequence:
                    vals['ref_customer'] = sequence.next_by_id( )

        if ('ref_supplier' not in vals) or (vals.get('ref_supplier') in ('/', False)):
            if  vals.get('customer',False): 
                sequence = self.env.ref('deltatech_saga.sequence_ref_supplier')
                if sequence:
                    vals['ref_customer'] = sequence.next_by_id( )
        return super(res_partner, self).create( vals )


    @api.multi
    def write(self, vals):
        if ('ref_customer' in vals) and (vals.get('ref_customer') in ('/', False)):
            self.ensure_one()
            if self.customer:
                sequence = self.env.ref('deltatech_saga.sequence_ref_customer')
                if sequence:
                    vals['ref_customer'] = sequence.next_by_id( )
                    
        if ('ref_supplier' in vals) and (vals.get('ref_supplier') in ('/', False)):
            self.ensure_one()
            if self.supplier:
                sequence = self.env.ref('deltatech_saga.sequence_ref_supplier')
                if sequence:
                    vals['ref_supplier'] = sequence.next_by_id( )
        
        return super(res_partner, self).write( vals)
    
