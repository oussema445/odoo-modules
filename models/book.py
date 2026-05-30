from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author')
    date_published = fields.Date(string='Published Date')
    isbn = fields.Char(string='ISBN')
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ], string='Status', default='available')
    active = fields.Boolean(default=True)

    # Contrainte SQL — ISBN unique dans la DB
    _sql_constraints = [
        ('isbn_unique', 'UNIQUE(isbn)', 'ISBN must be unique !')
    ]

    # Contrainte Python — validation métier
    @api.constrains('isbn')
    def _check_isbn(self):
        for book in self:
            if book.isbn and len(book.isbn) not in [10, 13]:
                raise ValidationError(
                    'ISBN must be 10 or 13 characters long !'
                )

    def action_borrow(self):
        self.state = 'borrowed'

    def action_return(self):
        self.state = 'available'