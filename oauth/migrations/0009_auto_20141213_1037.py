# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0008_auto_20141213_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcred',
            old_name='client_secret',
            new_name='encrypt_clilent_secret',
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
