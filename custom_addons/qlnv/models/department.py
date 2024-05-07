from odoo import fields, models, api

class department(models.Model):
    _name = 'department'
    _description = ''
    # _rec_name = "department_name"
    
    name = fields.Char(string='Name department',required=True)
    manager_id = fields.Many2one('res.users',string='Manager')
    number_employee = fields.Integer(string='Employee', compute ='_compute_employees')
    employee_ids = fields.One2many('res.users','department_id', string='Employee')
    company_id = fields.Many2one('res.company', string='Company')
    
    # ip_config = fields.Char(string= 'IP config', compute = '_get_ip_config', default = '')
    ip_config_id = fields.Many2one('timekeeping', string= 'IP config')
    
    @api.onchange('name')
    def _compute_employees(self): 
        for rec in self:
            if rec:
                a = self.env['res.users'].search([('department_id','=',rec.id)])
                rec.number_employee = len(a)
        
    
    def get_employee(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window'].sudo()._for_xml_id('qlnv.employee_action1')
        action['domain'] = [('department_id','=',self.id)]
        return action
    
    @api.depends('name')
    def _get_ip_config(self):
        for i in self:
            a = self.env['timekeeping'].search([('department_id', '=', i.id)])
            for rec in a:
                if rec:
                    if rec.is_active == True:
                        self.ip_config = rec.config_ip
                    else :
                        self.ip_config = ''
                else:
                    self.ip_config = ''
    
        
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Employee list',
        #     'view_mode': 'tree,form',
        #     "views": [["employee_view_tree", "tree"], ["employee_view_form", "form"]],
        #     "res_id": a_product_id,
        #     'res_model': 'res.users',
        #     'domain': [('department_name','=',self.id)],
        #     'context': "{'create': true}"
        # }
        
        