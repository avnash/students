# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0009_auto_20141220_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginrequestlog',
            name='get_data',
        ),
        migrations.RemoveField(
            model_name='loginrequestlog',
            name='post_data',
        ),
    ]
