# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0011_auto_20141213_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('responsetype', models.CharField(default=b'code', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='usertype',
            old_name='type',
            new_name='usertype',
        ),
        migrations.AddField(
            model_name='client',
            name='responsetypes',
            field=models.ManyToManyField(to='oauth.ResponseType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userauthlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 10, 47, 18, 250839)),
            preserve_default=True,
        ),
    ]
