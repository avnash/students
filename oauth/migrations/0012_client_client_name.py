# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0011_userlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_name',
            field=models.CharField(default=b'a', max_length=40),
            preserve_default=True,
        ),
    ]
