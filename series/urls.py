from django.conf.urls import url

from . import views

app_name = "series"

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/(?P<stat>[\w]+)?/?$', views.detail, name="detail")
]
