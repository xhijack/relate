# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-22 20:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0082_alter_models_for_preapproval_by_inst_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
    ]