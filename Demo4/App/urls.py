from django.conf.urls import url
from App import views


urlpatterns = [
    url(r'^index/',views.index, name='index'),
    url(r'^uploadfile/',views.upload_file,name='uploadfile'),
    url(r'^download/(?P<file_name>.*)', views.download_file,name='downloadfile'),
]