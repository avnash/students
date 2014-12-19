# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_client_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(to='oauth.User'),
            preserve_default=True,
        ),
    ]
