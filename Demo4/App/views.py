# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Demo4 import settings
import os
from django.http import StreamingHttpResponse

# Create your views here.
def index(request):
    files = []
    for f in os.listdir(settings.CACHE_ROOT):
        files.append(f)
    return render(request, 'index.html', context={'files': files})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        f = open(os.path.join(settings.BASE_DIR,'static', 'upload', file.name), 'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return redirect('/app/index')


def download_file(request, file_name):
    print('-----------')
    print(file_name)
    print('-----------')
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:

            if f:
                yield f.read(chunk_size)
                print('下载完成')
            else:
                print('未完成下载')

    the_file_name = os.path.join(settings.CACHE_ROOT, file_name)
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachement;filename="{0}"'.format(file_name)
    return response























