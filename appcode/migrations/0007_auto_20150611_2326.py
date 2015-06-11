# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0006_auto_20150611_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='image',
            field=models.TextField(null=True, blank=True),
        ),
    ]
