from odoo import models, fields, api, _, _lt
import re
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo.http import request

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
    
    attendances_ids = fields.One2many('attendances','employee_id',string='Attendances')
    attendances_number_id = fields.Many2one('attendances',string='Attendances')
    
    @api.onchange('name')
    def check_duplicate_name(self):
        rec = request.env['res.users'].sudo().search([('name','=ilike',self.name)])
        if rec:
            raise ValidationError(_('Users already exists, please re-enter.'))
        
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
    
    @api.model
    def get_model_data(self):
            records = self.env['res.users'].search([('id','=',self.env.uid)])
            status = 'check_in'
            data_users = []
            check_date = fields.Datetime.now().date().strftime('%Y-%m-%d')
            attendances = self.env['attendances'].search([('employee_id','=',self.env.uid),('create_date','>=',check_date)])

            if attendances:
                for rec in attendances:
                    status = rec.status
                        
            for rec in records:
                data_users.append({
                    'id': rec.id,
                    'name': rec.name,
                    'status': status,
                    'image': rec.image_employee,
                })
            return data_users
        
    @api.model
    def create_attendances(self):
        check_date = fields.Datetime.now().date().strftime('%Y-%m-%d')
        attendances = self.env['attendances'].search([('employee_id','=',self.env.uid),('create_date','>=',check_date)])
        
        if attendances:
            for rec in attendances:
                    rec.write({'check_out':fields.Datetime.now()})
                    return rec
        else:
            val = {
                    'employee_id':self.env.uid,
                    'check_in': fields.Datetime.now(),
                    'status':'check_out'
            }
            self.env['attendances'].create(val)
            
        return attendances  