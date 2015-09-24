# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VotingPlatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndrewIDs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('andrewId', models.CharField(max_length=20)),
                ('first_voted', models.BooleanField(default=False)),
                ('second_voted', models.BooleanField(default=False)),
                ('is_judge', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='votes_judge',
            field=models.IntegerField(default=0),
        ),
    ]
