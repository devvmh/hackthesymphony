# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='youtube_embed_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='highlights',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='image',
            field=models.URLField(null=True, blank=True),
        ),
    ]
