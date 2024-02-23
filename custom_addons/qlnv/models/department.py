from odoo import fields, models, api

class department(models.Model):
    _name = 'department'
    _description = ''
    # _rec_name = "department_name"
    
    
    id = fields.Char(string= 'Id department', required=True)  
    name = fields.Char(string='Name department')
    manager_id = fields.Many2one('res.users',string='Manager')
    number_employee = fields.Integer(string='Employee', compute ='_compute_employees')
    employee_ids = fields.One2many('res.users','department_id', string='Employee')
    
    
    @api.onchange('name')
    def _compute_employees(self): 
        for rec in self:
            if rec:
                a = self.env['res.users'].search([('department_id','=',rec.id)])
                rec.number_employee = len(a)
        
    
    def get_employee(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window'].sudo()._for_xml_id('qlnv.employee_action')
        action['domain'] = [('department_id','=',self.id)]
        return action
    
    
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
        
        