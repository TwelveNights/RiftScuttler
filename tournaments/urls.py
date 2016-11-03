from django.conf.urls import url

from . import views

app_name = "tournaments"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>[A-Za-z\s]+)/(?P<year>[0-9]{4})/$', views.details, name="details"),
    url(r'^(?P<id>[A-Za-z\s]+)/(?P<year>[0-9]{4})/series/(?P<series>[0-9]+)/$', views.series, name="series"),
    url(r'^(?P<id>[A-Za-z\s]+)/(?P<year>[0-9]{4})/series/(?P<series>[0-9]+)/(?P<number>[0-9]{1})/$', views.match, name="match")
]
