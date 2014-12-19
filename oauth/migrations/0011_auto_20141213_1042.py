# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0010_auto_20141213_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='manager',
        ),
        migrations.AddField(
            model_name='client',
            name='managers',
            field=models.ManyToManyField(to='oauth.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 10, 42, 48, 749279)),
            preserve_default=True,
        ),
    ]
