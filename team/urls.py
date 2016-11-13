from django.conf.urls import url

from . import views

app_name = "team"

urlpatterns = [
    url(r'^(?P<id>[a-zA-z0-9]+)/$', views.team, name="team"),
]