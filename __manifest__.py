# -*- coding: utf-8 -*-
{
    'name': "Brandon",

    'summary': """
       This is 
       
       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Brandon IT Department - Mohammed Oudah",
    'website': "http://www.brandon-group.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/saleOrderReport.xml',
        # 'views/addvet_layout_old.xml',
        'views/addvet_layout.xml',
        'views/brandvet_layout.xml',
        'views/malven_layout.xml',
        'views/namavet_layout.xml',
        'views/farmeto_layout.xml',
        'views/maxvet_layout.xml',
        'views/hipro_layout.xml',
        'views/fertizone_layout.xml',
        'views/namavet_report_saleorder_document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
