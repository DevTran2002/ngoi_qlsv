from odoo import models, fields, api, _, _lt
import re
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class employee_model(models.Model):
    _inherit = "res.users"
    _description =""
    
    
    private_email = fields.Char(string='Private email')
    gender = fields.Selection([('male', 'Male'),
                            ('female','Female'),
                            ('other','Other')])
    department_id = fields.Many2one('department', string='Department')
    date_of_birth = fields.Date(string='Date of birth')
    address = fields.Char(string='Address')
    job = fields.Char(string='Job')
    # job_position_id = fields.Many2one('job.position', string='Job position')
    parent_id=fields.Many2one('res.users',string='Parent')
    image_employee = fields.Binary(string='Image')
    identification = fields.Char(string='Number identification')
    passport = fields.Char(string='Number passport')
    place_of_birth = fields.Char(string='Place of birth')
    marital = fields.Selection([('married','Married'),
                                ('no_married','No married'),
                                ('divorce','Divorce'),
                                ('other','Other')])
    children = fields.Integer(string='Children')
    emergency_contact = fields.Char(string='Emergency contact')
    emergency_phone = fields.Char(string='Emergency phone')

    certificate = fields.Char(string='Certificate')
    study_school = fields.Char(string='Study school')
    start_work = fields.Date(string='Start work')
    time_works = fields.Integer(string='Time work')
    country_id = fields.Many2one('res.country',string='Country')
    
    number_department = fields.Integer(string='Department', compute = '_compute_department')
    number_employee = fields.Integer(string='', compute='_compute_employee')
    contract_type_id = fields.Many2one('contract.type', string='Contract type')
    

    def action_employee(self):
        action = self.env['ir.actions.act_window'].sudo()._for_xml_id('qlnv.employee_action')
        # action['domain'] = [('employee_ids','=',self.id)]
        return action
    
    @api.onchange('name')
    def _compute_department(self):
        for rec in self:
            if rec:
                a = self.env['department'].search([])
                rec.number_department = len(a)
        
    
    @api.onchange('name')
    def _compute_employee(self):
        for rec in self:
            if rec:
                temp = self.search([])
                rec.number_employee = len(temp)
                
                
    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise UserError(_('Please Enter Correct Email'))
    
    @api.onchange('phone')
    def validate_phone(self):
        if self.phone:
            match = re.match('^(\+84|84|0)+([0-9]{9})$', self.phone)
            if not match:
                raise ValidationError(_('Invalid Phone. Please re-enter.'))
    
    def get_department(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window'].sudo()._for_xml_id('qlnv.department_action')
        # action['domain'] = [('employee_ids','=',self.id)]
        return action
    
    
    
    