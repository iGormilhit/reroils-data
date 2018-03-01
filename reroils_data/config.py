# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 RERO.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""rero21 ils data module."""

# TODO: This is an example file. Remove it if your package does not use any
# extra configuration variables.

REROILS_DATA_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

REROILS_DATA_BASE_TEMPLATE = 'reroils_data/base.html'
"""Default base template for the demo page."""

REROILS_DATA_IMPORT_BNF_EAN = 'http://catalogue.bnf.fr/api/SRU?'\
    'version=1.2&operation=searchRetrieve'\
    '&recordSchema=unimarcxchange&maximumRecords=1'\
    '&startRecord=1&query=bib.ean%%20all%%20"%s"'
