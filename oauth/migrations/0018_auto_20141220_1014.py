# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0017_auto_20141219_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauthlog',
            name='trashed_at',
            field=models.DateTimeField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 10, 14, 19, 237501)),
            preserve_default=True,
        ),
    ]
