# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-03 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenotypedb', '0022_rnaseq_rnaseqvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='rnaseq',
            name='growth_conditions',
            field=models.TextField(blank=True, null=True),
        ),
    ]