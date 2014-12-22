# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0004_auto_20141220_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_data', models.CharField(max_length=99999)),
                ('get_data', models.CharField(max_length=99999)),
                ('post_data', models.CharField(max_length=99999)),
                ('user', models.ForeignKey(to='oauth.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
