# -*- coding: utf-8 -*-
{
    'name': "Hide Odoo Brand In User Account Menu",
    'version': '13.0.1.0',
    'license': 'LGPL-3',
    'category': 'Tools',
    "author": "Waqar Ahmad",
    "website": "https://www.linkedin.com/in/waqar-ahmad-62b473230/",
    'company': 'Waqar Ahmad',
    'maintainer': 'Waqar Ahmad',

    'summary': """Remove Documentation, Support, My Odoo.com account from the top right corner""",
    'description': """ Remove Documentation, Support, My Odoo.com account from the top right corner """,

    'depends': ['base'],
    'qweb': ['static/src/xml/base.xml'],

    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
