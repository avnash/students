# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_auto_20141213_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauthlog',
            name='auth_code',
            field=models.CharField(default=b'auth_code', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userauthlog',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 10, 16, 15, 659569)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userauthlog',
            name='trash',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 10, 16, 15, 659631)),
            preserve_default=True,
        ),
    ]
