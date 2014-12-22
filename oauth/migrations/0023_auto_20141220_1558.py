# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0022_auto_20141220_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostel_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='hostel',
            field=models.ForeignKey(default=0, to='oauth.Hostel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
