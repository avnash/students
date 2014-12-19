# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0006_auto_20141213_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='scopename',
            new_name='scope',
        ),
        migrations.RenameField(
            model_name='usertype',
            old_name='typename',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='access_token',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
