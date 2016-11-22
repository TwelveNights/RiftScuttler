from django.conf.urls import url

from . import views

app_name = "tournaments"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>[\w]+)/$', views.detail, name="detail")
]
