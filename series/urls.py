from django.conf.urls import url

from . import views

app_name = "series"

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.detail, name="detail")
    # url(r'^(?P<id>[0-9]+)/(?P<number>[0-9]{1})/$', views.match, name="match")
]
