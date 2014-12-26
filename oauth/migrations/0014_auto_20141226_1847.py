# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0013_auto_20141226_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcred',
            name='client_secret',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
