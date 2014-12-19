# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0012_auto_20141213_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userauthlog',
            name='client',
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 15, 58, 21, 671287)),
            preserve_default=True,
        ),
    ]
