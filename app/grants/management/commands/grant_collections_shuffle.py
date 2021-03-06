# -*- coding: utf-8 -*-
"""Define the Grant subminer management command.

Copyright (C) 2020 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""

import random

from django.core.management.base import BaseCommand

from grants.models import GrantCollection


class Command(BaseCommand):

    help = 'grant collection shuffle'

    def handle(self, *args, **options):
        for gc in GrantCollection.objects.filter(hidden=False):
            gc.shuffle_rank = random.randint(0,99999)
            gc.save()
        print('done')
