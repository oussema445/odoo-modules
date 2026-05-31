from odoo import models, fields

class Employee(models.Model):
    _name = 'hr.employee.custom'
    _description = 'Employee'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    hire_date = fields.Date(string='Hire Date')
    department_id = fields.Many2one('hr.department.custom', string='Department')
    state = fields.Selection([
        ('active', 'Active'),
        ('resigned', 'Resigned'),
    ], string='Status', default='active')
    active = fields.Boolean(default=True)

    def action_resign(self):
        self.state = 'resigned'
        self.active = False
