# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Echeance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50, unique=True)),
                ('adherent_name', models.CharField(max_length=250)),
                ('adherent_id', models.CharField(max_length=10)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('operation_date', models.DateField()),
                ('cyclos_payment_id', models.CharField(blank=True, max_length=50)),
                ('cyclos_error', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
