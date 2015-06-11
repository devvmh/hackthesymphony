# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0007_auto_20150611_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.TextField(),
        ),
    ]
