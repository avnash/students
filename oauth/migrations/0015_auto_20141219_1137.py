# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0014_auto_20141219_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcred',
            old_name='encrypt_client_secret',
            new_name='client_secret',
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 11, 37, 18, 339915)),
            preserve_default=True,
        ),
    ]
