from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    brand_ids = fields.Many2one('product.brand', string='Brands')
