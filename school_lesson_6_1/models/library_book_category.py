from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book category"

    name = fields.Char("Title")
    description = fields.Text()
    book_ids = fields.One2many(
        comodel_name="library.book",
        inverse_name="category_id",
        required=False,
    )
