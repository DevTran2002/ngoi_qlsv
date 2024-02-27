from odoo import fields, models

class workLocation (models.Model):
    _name = "work.location"
    _description =''
    
    name = fields.Char(string='Work location' ,required=True)
    address_id = fields.Char(string='Work address')
    company_id = fields.Many2one('res.company', string='Company')
    
    
