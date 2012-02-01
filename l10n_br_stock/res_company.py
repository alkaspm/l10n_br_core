# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
# Copyright (C) 2011  Renato Lima - Akretion                                    #
#                                                                               #
#This program is free software: you can redistribute it and/or modify           #
#it under the terms of the GNU Affero General Public License as published by    #
#the Free Software Foundation, either version 3 of the License, or              #
#(at your option) any later version.                                            #
#                                                                               #
#This program is distributed in the hope that it will be useful,                #
#but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#GNU Affero General Public License for more details.                            #
#                                                                               #
#You should have received a copy of the GNU Affero General Public License       #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.          #
#################################################################################

from osv import osv, fields

class res_company(osv.osv):
    
    _inherit = "res.company"

    _columns = {
                'stock_fiscal_category_operation_id': fields.many2one('l10n_br_account.fiscal.operation.category', 
                                                                      'Categoria Fiscal Padrão Estoque',
                                                                      domain="[('use_picking','=',True)]"),
    }

res_company()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: