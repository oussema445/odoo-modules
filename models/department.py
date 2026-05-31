from odoo import models, fields

class Department(models.Model):
    _name = 'hr.department.custom'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    manager_id = fields.Many2one('hr.employee.custom', string='Manager')
    employee_ids = fields.One2many('hr.employee.custom', 'department_id', string='Employees')
    