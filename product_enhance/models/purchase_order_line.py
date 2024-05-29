from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    category_id = fields.Many2one('product.category', string='Category')
    brand_id = fields.Many2one('product.brand', string='Brand')
    model_id = fields.Many2one('product.model', string='Model')
    price_group_id = fields.Many2one('product.price.group', string='Price Group')

