# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0002_auto_20150602_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='protip',
            field=models.CharField(max_length=2550, blank=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='comment',
            field=models.CharField(max_length=2550, blank=True),
        ),
    ]
