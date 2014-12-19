# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0013_auto_20141213_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcred',
            old_name='encrypt_clilent_secret',
            new_name='encrypt_client_secret',
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 11, 36, 31, 404154)),
            preserve_default=True,
        ),
    ]
