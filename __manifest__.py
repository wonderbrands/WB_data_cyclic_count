# -*- coding: utf-8 -*-
{
    'name': "WB_data_cyclic_count",

    'summary': "Is able to count the amount of stock in the wharehouse", 

    'description': """
        Provides a frontend interface to count the 
        amount of stock in the wharehouse making use of a scanner 
        in a flow that asks for the ubication, the product and the quantity
    """,

    'author': "Wonderbrands",
    'website': "https://www.wonderbrands.co",
    'license': 'LGPL-3',
    'category': 'Inventory',
    'version': '18.0',
    
    'depends': [
        'base', 
        'stock',
        'product',
    ],

    'data': [
        "data/landscape_letter.xml",
        "data/groups.xml",
        "views/cycle_count_views.xml",
        "views/cycle_count_actions.xml",
        "views/cycle_count_menu.xml",
        "templates/barcodes.xml",
        "security/ir.model.access.csv",
        "data/default_waves.xml",
    ],

    'assets': {
        'web.assets_backend': [
            '/WB_data_cyclic_count/static/src/js/app/objs.js',
            '/WB_data_cyclic_count/static/src/js/CycleCount.js',
            '/WB_data_cyclic_count/static/src/css/CycleCount.scss',
        ],

        'web.assets_qweb': [
            '/WB_data_cyclic_count/static/src/xml/CycleCount.xml',
        ],
    }

}
