# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0007_auto_20141220_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginrequestlog',
            name='meta_data',
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_http_host',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_http_referer',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_http_user_agent',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_query_string',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_remote_addr',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_remote_host',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='meta_request_method',
            field=models.TextField(default=b'a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginrequestlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 18, 38, 45, 603192)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='username',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
