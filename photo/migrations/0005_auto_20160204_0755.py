# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20160204_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
