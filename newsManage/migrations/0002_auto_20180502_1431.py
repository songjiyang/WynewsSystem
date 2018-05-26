# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsinfo',
            name='viewPara',
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='newsLabel',
            field=models.CharField(default='\u5176\u4ed6', max_length=200),
        ),
    ]
