# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('votes_first_round', models.IntegerField(default=0)),
                ('votes_second_round', models.IntegerField(default=0)),
                ('information', models.CharField(max_length=8192)),
                ('picture', models.ImageField(upload_to=b'pictures', blank=True)),
                ('round', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField(default=1)),
                ('open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sessionid', models.CharField(max_length=128)),
                ('first_voted', models.BooleanField(default=False)),
                ('second_voted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TicketNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('first_voted', models.BooleanField(default=False)),
                ('second_voted', models.BooleanField(default=False)),
            ],
        ),
    ]
