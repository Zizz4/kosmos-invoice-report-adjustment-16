from odoo import fields, models, api


class AccountMoveRefDate(models.Model):
    _inherit = 'account.move'

    ref_date = fields.Date(string="PO Date")
