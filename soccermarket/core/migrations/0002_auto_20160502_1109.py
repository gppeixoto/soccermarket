# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='nameCompleto',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='imagemCamisa',
            new_name='kit_image',
        ),
    ]
