# -*- coding: utf-8 -*-
{
    'name': "goldenbakery",

    'summary': """
        oddoo module for Golden Bakery""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/menucake_view.xml',
        'views/categorycake_view.xml',
        'views/employee_view.xml',
        'views/chef_view.xml',
        'views/cashier_view.xml',
        'views/cleaningservice_view.xml',
        'views/customer_view.xml',
        'views/rawingridient_view.xml',
        'views/supplier_view.xml',
        'views/transaksi_view.xml',
        'report/report.xml',
        'report/print_faktur_transaksi.xml',
        'wizzard/tambahstokcake_wizzard_view.xml',
        'wizzard/inputstokbahanbaku_wizzard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
