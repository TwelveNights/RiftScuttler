from django.conf.urls import url

from . import views

app_name = "playerstatistics"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pname>[a-zA-Z0-9]{1,16})$', views.detailView, name="detail")
]
