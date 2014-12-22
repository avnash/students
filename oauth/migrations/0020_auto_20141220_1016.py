# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0019_auto_20141220_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 10, 16, 8, 904390)),
            preserve_default=True,
        ),
    ]
