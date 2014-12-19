# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0005_auto_20141213_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauthlog',
            name='access_token',
            field=models.CharField(default=b'access_token', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='auth_code',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
