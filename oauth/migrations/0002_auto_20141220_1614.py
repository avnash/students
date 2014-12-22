# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_squashed_0028_auto_20141220_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
    ]
