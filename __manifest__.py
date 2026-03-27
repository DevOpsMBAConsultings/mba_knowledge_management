{
    "name": "Knowledge Management",
    'summary': "A fast, organized, collaborative knowledge hub inside Odoo community Edition",
    'description': """
        A fast, organized, collaborative knowledge hub inside Odoo community Edition.
    """,
    'version': "19.0.1.0.0",
    "author": "MBA Consultings",
    "company": "MBA Consultings",
    "maintainer": "MBA Consultings",
    "website": "http://mbaconsultings.com",
    "support": "contact@mbaconsultings.com",
    "license": "LGPL-3",
    "category": "Knowledge",
    "depends": ["base", "mail", "web", 'hr'],
    "data": [
        "security/ir.model.access.csv",
        "security/knowledge_security.xml",
        "views/knowledge_views.xml",
        "views/knowledge_menus.xml",
        "views/article_public_template.xml",
    ],
    "assets": {
    "web.assets_backend": [
        "mba_knowledge_management/static/src/js/knowledge_split.js",
        "mba_knowledge_management/static/src/xml/knowledge_split_template.xml",
        "mba_knowledge_management/static/src/css/knowledge_split.css",
        "https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js",
        ]
    },
    "images": ["static/description/banner.gif"],
    "installable": True,
    "application": True,
    'price': 0.00,
    'currency': 'USD',
}