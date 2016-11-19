from django.conf.urls import url

from . import views


app_name = "champions"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cid>[\d]{1,16})$', views.detailView, name="detail")
]
