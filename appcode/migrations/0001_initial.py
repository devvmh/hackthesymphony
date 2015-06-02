# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=2550)),
                ('comment', models.CharField(max_length=2550, blank=True)),
                ('redirect_url_if_no_new_question', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=2550)),
                ('date', models.DateField()),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('highlights', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConcertAnswerScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('answer', models.ForeignKey(to='appcode.Answer')),
                ('concert', models.ForeignKey(to='appcode.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255, blank=True)),
                ('ip', models.CharField(max_length=15)),
                ('current_question', models.ForeignKey(default=1, blank=True, to='appcode.Question')),
            ],
        ),
        migrations.CreateModel(
            name='SessionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.ForeignKey(related_name='sessions_using_this_answer', to='appcode.Answer')),
                ('question', models.ForeignKey(related_name='sessions_answered_this_question', to='appcode.Question')),
                ('session', models.ForeignKey(related_name='answers', to='appcode.Session')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='new_question',
            field=models.ForeignKey(related_name='answer_leading_here', blank=True, to='appcode.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='old_question',
            field=models.ForeignKey(related_name='answers', to='appcode.Question'),
        ),
    ]
