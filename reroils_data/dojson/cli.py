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

"""Click command-line utilities."""

from __future__ import absolute_import, print_function

import json
import re
from pathlib import Path

import click
from flask import current_app
from flask.cli import with_appcontext
from flask_security.confirmable import confirm_user
from invenio_accounts.cli import commit, users
from invenio_pidstore.models import PersistentIdentifier
from werkzeug.local import LocalProxy

from reroils_data.documents_items.cli import create_items
from reroils_data.organisations_members.cli import import_organisations

_datastore = LocalProxy(lambda: current_app.extensions['security'].datastore)


@click.group()
def fixtures():
    """Fixtures management commands."""

fixtures.add_command(import_organisations)
fixtures.add_command(create_items)


@click.command('reverse')
def reverse():
    """Reverse the order of the data."""
    def processor(iterator):
        items = []
        for item in iterator:
            items.append(item)
        items.reverse()
        return items

    return processor


@click.command('head')
@click.argument('max', type=click.INT,)
def head(max):
    """Take only the first max items."""
    def processor(iterator):
        n = 0
        for item in iterator:
            if n >= max:
                raise StopIteration
            n += 1
            yield item

    return processor
