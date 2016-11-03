from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pid>[0-9]{1,3})$', views.playdetail)
]