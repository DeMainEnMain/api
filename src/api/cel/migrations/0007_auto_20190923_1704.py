# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-23 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cel', '0006_create_predefined_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='securityanswer',
            old_name='question',
            new_name='question_fk',
        ),
    ]
