# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0005_loginrequestlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginrequestlog',
            name='user',
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='username',
            field=models.CharField(default=b'a', max_length=99999),
            preserve_default=True,
        ),
    ]
