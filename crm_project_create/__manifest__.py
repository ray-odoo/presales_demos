# Copyright 2024 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)
# modified by Odoo MMC Valencia to support Project Templates 
# and remove dependency on email module

{
    "name": "CRM Project Create",
    "summary": "Allow create projects from lead/opportunity",
    "version": "1.0",
    "category": "Sales/CRM",
    "website": "https://github.com/OCA/crm",
    "author": "Moduon, Odoo Community Association (OCA)",
    "maintainers": ["EmilioPascual", "rafaelbn"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["crm", "sale_project"],
    "data": [
        "views/crm_lead.xml",
        "views/project_project.xml",
    ],
}
