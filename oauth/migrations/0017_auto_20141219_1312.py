# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0016_auto_20141219_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userauthlog',
            old_name='auth_code',
            new_name='authorization_code',
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 13, 12, 32, 147603)),
            preserve_default=True,
        ),
    ]
