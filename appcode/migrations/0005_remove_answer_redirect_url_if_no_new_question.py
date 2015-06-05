# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0004_session_session_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='redirect_url_if_no_new_question',
        ),
    ]
