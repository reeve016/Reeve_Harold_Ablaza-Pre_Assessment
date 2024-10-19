from odoo import models, fields

# Task 2: Add an author field to the book model
class LibraryBook(models.Model):
    _inherit = "library.book"
    author_id = fields.Many2one('res.partner', required=True, string="Author")
   

   # Task 3: Add an author field to the book model - Part 2
    category_id = fields.Many2many('library.book.category', string="Category")
