# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-01-31 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='static_files/uploaded'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='static_files/uploaded'),
        ),
    ]