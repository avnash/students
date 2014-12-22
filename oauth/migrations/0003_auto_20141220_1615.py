# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20141220_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hostel',
            field=models.ForeignKey(default=1, to='oauth.Hostel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
