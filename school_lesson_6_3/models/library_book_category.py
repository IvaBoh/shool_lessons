from odoo import models, _


class LibraryBookCategory(models.Model):
    """
    This class inherits from the category class that resides
    in module school_lesson_6_1.
    """

    _inherit = "library.book.category"

    def action_show_book_list(self):
        """This method shows all books of a certain category."""
        self.ensure_one()
        return {
            "name": _("Books of the category"),
            "type": "ir.actions.act_window",
            "view_mode": "tree",
            "res_model": "library.book",
            "context": {"default_category_id": self.id},
            "domain": [("category_id", "=", self.id)],
        }
