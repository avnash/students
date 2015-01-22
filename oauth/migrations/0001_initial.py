# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(max_length=40)),
                ('client_uri', models.CharField(max_length=200)),
                ('client_name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientCred',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_secret', models.CharField(max_length=40)),
                ('client', models.ForeignKey(to='oauth.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='LoginRequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField()),
                ('meta_http_host', models.TextField()),
                ('meta_http_referer', models.TextField()),
                ('meta_http_user_agent', models.TextField()),
                ('meta_query_string', models.TextField()),
                ('meta_remote_addr', models.TextField()),
                ('meta_remote_host', models.TextField()),
                ('meta_request_method', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scope', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('room', models.IntegerField(default=0)),
                ('hostel', models.ForeignKey(to='oauth.Hostel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAuthLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorization_code', models.CharField(max_length=40)),
                ('access_token', models.CharField(max_length=60)),
                ('trash', models.IntegerField(default=0)),
                ('expiry', models.DateTimeField()),
                ('ip', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(to='oauth.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCred',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encrypt_key', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to='oauth.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField()),
                ('count', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usertype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertype', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='usertypes',
            field=models.ManyToManyField(to='oauth.Usertype'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='managers',
            field=models.ManyToManyField(to='oauth.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='responsetypes',
            field=models.ManyToManyField(to='oauth.ResponseType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='scopes',
            field=models.ManyToManyField(to='oauth.Scope'),
            preserve_default=True,
        ),
    ]
