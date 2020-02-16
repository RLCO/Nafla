# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    purchase_request_id = fields.Many2one('sprogroup.purchase.request')