# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('newsType', models.CharField(max_length=50)),
                ('newsTile', models.CharField(max_length=200)),
                ('newsDateTime', models.CharField(max_length=50)),
                ('viewPicturePath', models.CharField(max_length=500)),
                ('viewPara', models.CharField(max_length=3000)),
                ('content', models.TextField()),
                ('priKey', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
    ]
