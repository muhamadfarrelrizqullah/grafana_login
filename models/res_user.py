from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')

    @api.model
    def create(self, vals):
        user = super(ResUsers, self).create(vals)
        return user