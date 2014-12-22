# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0008_auto_20141220_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_http_host',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_http_referer',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_http_user_agent',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_query_string',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_remote_addr',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_remote_host',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='meta_request_method',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginrequestlog',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
