# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0024_auto_20141220_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hostel',
            field=models.ForeignKey(default=b'default', to='oauth.Hostel'),
            preserve_default=True,
        ),
    ]