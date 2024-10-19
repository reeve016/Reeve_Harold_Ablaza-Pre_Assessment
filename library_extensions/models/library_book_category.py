

from odoo import models, fields

# Task 3: Create a book category model - PART 1
class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"
    name = fields.Char(required=True, unique=True, string = 'Name')
    