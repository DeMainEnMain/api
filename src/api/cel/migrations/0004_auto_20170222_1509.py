# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cel', '0003_create_predefined_questions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='beneficiaire',
            unique_together=set([('owner', 'cyclos_account_number')]),
        ),
    ]
