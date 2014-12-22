# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0020_auto_20141220_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 10, 18, 40, 31471)),
            preserve_default=True,
        ),
    ]
