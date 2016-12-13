"""RiftScuttler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import curator_home, logout_view, add_data_page, remove_data_page, edit_data_page, view_data_page
from .helpers import get_nav_list_raw


urlpatterns = [
        url(r'^$', curator_home, name='curator-home'),
        url(r'^logout/$', logout_view, name='logout-page'),
]

urlpatterns_add = [url(r'^add_'+table_name+'/$', add_data_page,
                       name='add-'+table_name) for table_name in get_nav_list_raw()]
urlpatterns_remove = [url(r'^remove_' + table_name + '/$', remove_data_page,
                          name='remove-' + table_name) for table_name in get_nav_list_raw()]
urlpatterns_edit = [url(r'^edit_' + table_name + '/$', edit_data_page,
                        name='edit-' + table_name) for table_name in get_nav_list_raw()]
urlpatterns_view = [url(r'^view_' + table_name + '/$', view_data_page,
                        name='view-' + table_name) for table_name in get_nav_list_raw()]
urlpatterns.extend(urlpatterns_add)
urlpatterns.extend(urlpatterns_remove)
urlpatterns.extend(urlpatterns_edit)
urlpatterns.extend(urlpatterns_view)
