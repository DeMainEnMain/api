# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-30 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cel', '0010_auto_20190923_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mandat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_compte_debiteur', models.CharField(max_length=9)),
                ('nom_debiteur', models.CharField(max_length=150)),
                ('numero_compte_crediteur', models.CharField(max_length=9)),
                ('nom_crediteur', models.CharField(max_length=150)),
                ('statut', models.CharField(choices=[('ATT', 'En attente de validation'), ('VAL', 'Validé'), ('REF', 'Refusé'), ('REV', 'Révoqué')], default='ATT', max_length=3)),
            ],
            options={
                'db_table': 'mandat',
            },
        ),
        migrations.AlterUniqueTogether(
            name='mandat',
            unique_together=set([('numero_compte_crediteur', 'numero_compte_debiteur')]),
        ),
    ]