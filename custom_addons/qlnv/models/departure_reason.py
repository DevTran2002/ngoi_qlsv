from odoo import fields, models

class reason_for_quit (models.Model):
    _name = 'departure.reason'
    
    name = fields.Char(string='Reasons')
    sequence =fields.Integer(default = 0,string='sequence')
    