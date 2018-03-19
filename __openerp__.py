# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Modulo Hola Mundo',
    'version': '1.0',
    'author': ['Bryan Oviedo'],
    'category': 'Tools',
    'summary': 'Ejemplo de un módulo de Odoo',
    'website': 'https://www.google.com',
    'description': """
Ejemplo de Hola Mundo.
======================
Con este módulo mostraremos como hacer un componente en Odoo10
    """,
    'depends': ['base'],
    'data': [
        'modelo_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}