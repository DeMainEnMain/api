# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-23 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cel', '0004_auto_20170222_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredefinedSecurityQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('language', models.CharField(choices=[('eu', 'eu'), ('fr', 'fr')], max_length=2)),
            ],
            options={
                'db_table': 'predefined_security_question',
            },
        ),
    ]
