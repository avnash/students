# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0004_auto_20141213_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthlog',
            name='expiry',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
