# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "IPPay Payment Acquirer",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "summary": "IPPay Payment",
    "author": "Open Source Integrators",
    "maintainer": "Open Source Integrators",
    "website": "http://www.opensourceintegrators.com",
    "category": "Accounting",
    "depends": ['payment'],
    "data": [
        "data/ippay_payment_data.xml",
        "data/account_payment_method.xml",
        "views/payment_view.xml",
    ],
    "development_status": "beta",
    "installable": True,
    'external_dependencies': {'python': ['xmltodict']}
}
