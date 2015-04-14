# -*- coding: utf-8 -*-
{
    "name" : "Orchid Accounting Reports",
    "version" : "0.1",
    "author": "OrchidERP",
    "category" : "Accounting AND Finance",
    "description": """OrchidERP Accounting Reports""",
    "website": ["http://www.orchiderp.com"],
    "depends": ['report_webkit','orchid_report','orchid_cost_centre'],
    "data" : [
            'wizard/account_report_partner_ledger_view.xml',
            'wizard/account_report_general_ledger_view.xml',
            'wizard/account_report_account_balance_view.xml',
            ],
    'css': [],
}
