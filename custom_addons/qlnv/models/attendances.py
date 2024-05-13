from odoo import fields, api, models
from odoo.exceptions import AccessError
from odoo import models, fields, api, exceptions, _
from odoo.tools import format_datetime
from odoo.osv.expression import AND, OR
from datetime import datetime, timedelta

class attendances(models.Model):
    _name = 'attendances'
    _description= ''

    def _default_employee(self):
        res = self.env['res.users'].search([('id','=',self.env.user.id)])
        return res

    employee_id = fields.Many2one('res.users', string="Employee", default=_default_employee, required=True, ondelete='cascade', index=True)
    check_in = fields.Datetime(string= 'Check in', default=fields.Datetime.now, required=True)
    check_out = fields.Datetime(string= 'Check out')
    worked_hours = fields.Float(string='Worked hours', compute = '_worked_hours',store=True)
    face_recognition_ids = fields.One2many('hr.face.recognition','attendances_id',string='')
    
    def name_get(self):
        result = []
        for rec in self:
            if not rec.check_out:
                result.append((rec.id, _("%(empl_name)s from %(check_in)s") % {
                    'empl_name': rec.employee_id.name,
                    'check_in': format_datetime(self.env, rec.check_in, dt_format=False),
                }))
            else:
                result.append((rec.id, _("%(empl_name)s from %(check_in)s to %(check_out)s") % {
                    'empl_name': rec.employee_id.name,
                    'check_in': format_datetime(self.env, rec.check_in, dt_format=False),
                    'check_out': format_datetime(self.env, rec.check_out, dt_format=False),
                }))
        return result
    
    # def set_time_works(self):
    #     state = self.env['res.users'].search([('id', '=', self.env.user.id)]).attendances_status
        
    #     if state == True:
    #         name_get(self)
    
    
    
    @api.depends('check_out')
    def _worked_hours(self):
        if self.check_in and self.check_out:
            start_datetime = fields.Datetime.from_string(self.check_in)
            end_datetime = fields.Datetime.from_string(self.check_out)
            time_difference = end_datetime - start_datetime
            difference_in_seconds = time_difference.total_seconds()
            self.worked_hours = difference_in_seconds / 3600.0
        else:
            self.worked_hours = 0
            
    @api.constrains('check_in', 'check_out')
    def _check_validity_check_in_check_out(self):
        """ verifies if check_in is earlier than check_out. """
        for rec in self:
            if rec.check_in and rec.check_out:
                if rec.check_out < rec.check_in:
                    raise exceptions.ValidationError(_('"Check Out" time cannot be earlier than "Check In" time.'))