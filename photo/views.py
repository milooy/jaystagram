# coding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Photo # 동일 디렉토리에 있는 models.py
from .forms import PhotoEditForm


def single_photo(request, photo_id): # 인자가 여러 개라면 넘겨받은 순서대로 args에 배열로 담김
    photo = get_object_or_404(Photo, pk=photo_id) #첫 번째 인자로 모델 그 뒤론 탐색 키워드 인자
    photo = Photo.objects.get(pk=photo_id)
    response_text = '<p>{photo_id}번 사진</p>'
    response_text += '<img src="{photo_url}">'

    return HttpResponse(response_text.format(
        photo_id=photo_id,
        photo_url=photo.image_file.url))


def new_photo(request):
    if request.method == 'GET':
        edit_form = PhotoEditForm()
    elif request.method == 'POST':
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save()

            return redirect(new_photo.get_absolute_url())

    return render(
        request, # 뷰 함수는 언제나 첫 번째 인자로 request객체를 전달받음
        'new_photo.html', # 템플릿 파일 이름
        {
            'form': edit_form, # 템플릿 맥락 요소
        }
    )

