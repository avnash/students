# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0021_auto_20141220_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
