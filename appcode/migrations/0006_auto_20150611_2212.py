# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcode', '0005_remove_answer_redirect_url_if_no_new_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionanswer',
            name='question',
            field=models.ForeignKey(related_name='session_answers', to='appcode.Question'),
        ),
        migrations.AlterField(
            model_name='sessionanswer',
            name='session',
            field=models.ForeignKey(related_name='session_answers', to='appcode.Session'),
        ),
    ]
