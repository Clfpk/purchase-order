from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Brand')
    model_id = fields.Many2one('product.model', string='Model')
    price_group_id = fields.Many2one('product.price.group', string='Price Group', compute='_compute_price_group')

    @api.depends('brand_id', 'model_id')
    def _compute_price_group(self):
        for product in self:
            # Compute price group based on brand and model
            product.price_group_id = ...
