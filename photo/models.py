# coding: utf-8

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.conf import settings


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image_file = models.ImageField(upload_to='%Y/%m/%d')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d') #뭔가 얘때매 pip install Pillow를 했는데 다른곳에 추가 안해도 되나
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})