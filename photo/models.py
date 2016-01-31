# coding: utf-8

from __future__ import unicode_literals

from django.db import models


class Photo(models.Model):
    image_file = models.ImageField()
    filtered_image = models.ImageField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
