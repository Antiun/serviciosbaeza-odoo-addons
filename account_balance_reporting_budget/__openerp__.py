# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Budget capabilities for account balance reporting engine',
    'version': '1.0',
    'category': 'Account',
    'author': 'Serv. Tecnol. Avanzados - Pedro M. Baeza',
    'website': 'http://www.serviciosbaeza.com',
    'depends': [
        'account_balance_reporting',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_balance_reporting_template_view.xml',
        'views/account_balance_reporting_view.xml',
    ],
    "installable": True,
}
