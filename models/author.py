from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    bio = fields.Text(string='Biography')
    book_ids = fields.One2many('library.book', 'author_id', string='Books')
    book_count = fields.Integer(compute='_compute_book_count', string='Number of Books')

    def _compute_book_count(self):
        for author in self:
            author.book_count = len(author.book_ids)