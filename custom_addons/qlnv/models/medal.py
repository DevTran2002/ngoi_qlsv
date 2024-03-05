from  odoo import fields , models

class medal (models.Model):
    _name = 'game.badge'
    _inherit = 'image.mixin'
    
    name = fields.Char(string= 'Medal', required=True)
    description = fields.Html(string='Description')
    image = fields.Image(string='Image')

    rule_auth = fields.Selection([('everyone', 'Mọi người'),
                                ('users', 'Danh sách người được chọn'),
                                ('having','Người có một số huy hiệu'),
                                ('nobody','Không có ai')])
    rule_max = fields.Boolean(string='Số lượng giới hạn mỗi tháng')
    rule_max_number = fields.Integer(string='Số lượng giới hạn')
    rule_auth_user_ids =fields.Many2many('res.users',string='Người dùng được ủy quyền')
    rule_auth_badge_id = fields.Many2one('game.badge', string='Huy hiệu yêu cầu')
    