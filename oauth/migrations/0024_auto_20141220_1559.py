# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0023_auto_20141220_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hostel',
            field=models.ForeignKey(default=1, to='oauth.Hostel'),
            preserve_default=True,
        ),
    ]
