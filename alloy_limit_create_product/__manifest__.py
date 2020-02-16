# -*- coding: utf-8 -*-
{
    'name': "Alloy limit product creation",
    'summary': """Alloy limit product creation""",
    'description': """Alloy limit product creation""",
    'author': "Magdy, helcon",
    'website': "http://www.yourcompany.com",
    'category': 'stock',
    'version': '0.1',
    'depends': ['base', 'stock', 'sale'],
    'data': [
        'security/security.xml',
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/account_product_product_view.xml',
        'views/sales_product_varient_view.xml',
        'views/sale_order_view.xml',
        'views/account_invoice_view.xml',
        'views/purchase_order_view.xml',
        'views/crm_lead_view.xml',
    ],
}
