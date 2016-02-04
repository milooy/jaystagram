# coding: utf-8

from __future__ import unicode_literals
from django import forms
from .models import Photo


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('filtered_image', )
        # fields = '__all__' #에러나서 추가함
