# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0006_auto_20141220_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrequestlog',
            name='get_data',
            field=models.TextField(max_length=99999),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_data',
            field=models.TextField(max_length=99999),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='post_data',
            field=models.TextField(max_length=99999),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='username',
            field=models.TextField(default=b'a', max_length=99999),
            preserve_default=True,
        ),
    ]
