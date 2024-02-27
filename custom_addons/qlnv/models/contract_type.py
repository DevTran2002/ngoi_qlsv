from odoo import fields, models 


class contract_type(models.Model):
    _name = 'contract.type'
    
    sequence =fields.Integer(default = 0,string='sequence')
    name = fields.Char(string= 'Name')