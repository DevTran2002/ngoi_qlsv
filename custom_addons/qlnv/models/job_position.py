from odoo import fields, models

class job_position(models.Model):
    _name = 'job.position'

    name = fields.Char(string='Position', required=True)
    sequence =fields.Integer(default = 0,string='sequence')
    department_id = fields.Many2one('department', string='Department')
    contract_type_id = fields.Many2one('contract.type', string='Contract type')
    no_of_recruitment = fields.Integer(string='Target',default = '1')
    job_summary = fields.Html(string='Description')
    no_of_employee = fields.Integer(string='No of employee', compute = '_compute_no_of_employee')
    company_id = fields.Many2one('res.company', string='Company')
    user_id = fields.Many2one('res.users', string='Employer')
    
    # interviewer_ids = fields.One2many('res.users','job_position_id', string='Interviewer')
    
    def _compute_no_of_employee(self):
        for rec in self:
            if rec:
                a = self.env['job.position'].search([('id','=',rec.id)]).department_id.number_employee
                rec.no_of_employee = a
                
                