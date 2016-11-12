from django.conf.urls import url

from . import views

app_name = "tournaments"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>[\w]+)/$', views.details, name="details"),
    url(r'^(?P<id>[\w]+)/(?P<series>[0-9]+)/$', views.series, name="series"),
    url(r'^(?P<id>[\w]+)/(?P<series>[0-9]+)/(?P<number>[0-9]{1})/$', views.match, name="match")
]
