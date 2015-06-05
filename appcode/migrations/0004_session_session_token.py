# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0003_auto_20150602_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='session_token',
            field=models.CharField(default='INVALID_SESSION_TOKEN', max_length=255),
            preserve_default=False,
        ),
    ]
