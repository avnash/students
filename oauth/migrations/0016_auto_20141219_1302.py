# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0015_auto_20141219_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthlog',
            name='access_token',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='auth_code',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 13, 2, 45, 68396)),
            preserve_default=True,
        ),
    ]
