from odoo import api, models, fields,_, _lt
import socket
import ipaddress
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class Time_keeping(models.Model):
    _name = 'timekeeping'
    _description = ''

    
    name = fields.Char(string='Name',required=True)
    config_ip  = fields.Char(string= 'Config', default = '',)
    department_id = fields.Many2one('department', string= 'Department',required=True)
    is_active = fields.Boolean(string= 'Active?')
    
    def get_ip(self):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        self.config_ip = IPAddr

        
    @api.constrains('is_active')
    def check_active_ip(self):
        for rec in self:
            if rec:
                a = self.env['timekeeping'].search(['&',('department_id', '=', rec.department_id.id), ('is_active', '=', True)])
                if len(a) > 1:
                    raise UserError(_('Only 1 IP can be configured'))
    
    @api.onchange('config_ip')
    def ping_ip(self):
        if self.config_ip != '':
            try:
                print(ipaddress.ip_address(self.config_ip))
            except ValueError:
                raise UserError(_('IP is not a valid IP address.'))
                get_ip(self)