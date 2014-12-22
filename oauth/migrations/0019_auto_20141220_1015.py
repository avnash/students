# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0018_auto_20141220_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userauthlog',
            name='trashed_at',
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 10, 15, 20, 904427)),
            preserve_default=True,
        ),
    ]
