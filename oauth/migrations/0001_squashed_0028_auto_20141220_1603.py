# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'oauth', '0001_initial'), (b'oauth', '0002_client_manager'), (b'oauth', '0003_auto_20141213_1010'), (b'oauth', '0004_auto_20141213_1016'), (b'oauth', '0005_auto_20141213_1016'), (b'oauth', '0006_auto_20141213_1024'), (b'oauth', '0007_auto_20141213_1025'), (b'oauth', '0008_auto_20141213_1032'), (b'oauth', '0009_auto_20141213_1037'), (b'oauth', '0010_auto_20141213_1041'), (b'oauth', '0011_auto_20141213_1042'), (b'oauth', '0012_auto_20141213_1047'), (b'oauth', '0013_auto_20141213_1558'), (b'oauth', '0014_auto_20141219_1136'), (b'oauth', '0015_auto_20141219_1137'), (b'oauth', '0016_auto_20141219_1302'), (b'oauth', '0017_auto_20141219_1312'), (b'oauth', '0018_auto_20141220_1014'), (b'oauth', '0019_auto_20141220_1015'), (b'oauth', '0020_auto_20141220_1016'), (b'oauth', '0021_auto_20141220_1018'), (b'oauth', '0022_auto_20141220_1020'), (b'oauth', '0023_auto_20141220_1558'), (b'oauth', '0024_auto_20141220_1559'), (b'oauth', '0025_auto_20141220_1559'), (b'oauth', '0026_auto_20141220_1601'), (b'oauth', '0027_auto_20141220_1602'), (b'oauth', '0028_auto_20141220_1603')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(max_length=40)),
                ('client_uri', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientCred',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_secret', models.CharField(max_length=200)),
                ('client', models.ForeignKey(to='oauth.Client')),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAuthLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(to='oauth.User')),
                ('authorization_code', models.CharField(max_length=40)),
                ('expiry', models.DateTimeField()),
                ('trash', models.IntegerField(default=0)),
                ('access_token', models.CharField(max_length=60)),
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
            field=models.ManyToManyField(to=b'oauth.Usertype'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='scopes',
            field=models.ManyToManyField(to=b'oauth.Scope'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='managers',
            field=models.ManyToManyField(to=b'oauth.User'),
            preserve_default=True,
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
        migrations.AddField(
            model_name='client',
            name='responsetypes',
            field=models.ManyToManyField(to=b'oauth.ResponseType'),
            preserve_default=True,
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
