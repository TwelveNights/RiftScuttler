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
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', form_home),
    url(r'^$', login_page),
    url(r'^add_tournaments/$', add_data_page),
    url(r'^remove_tournaments/$', remove_data_page),
    url(r'^edit_tournaments/$', edit_data_page),
    url(r'^add_series/$', add_data_page),
    url(r'^remove_series/$', remove_data_page),
    url(r'^edit_series/$', edit_data_page),
    url(r'^add_champions/$', add_data_page),
    url(r'^remove_champions/$', remove_data_page),
    url(r'^edit_champions/$', edit_data_page),
    url(r'^add_items/$', add_data_page),
    url(r'^remove_items/$', remove_data_page),
    url(r'^edit_items/$', edit_data_page),
    url(r'^add_players/$', add_data_page),
    url(r'^remove_players/$', remove_data_page),
    url(r'^edit_players/$', edit_data_page),
    url(r'^add_teams/$', add_data_page),
    url(r'^remove_teams/$', remove_data_page),
    url(r'^edit_teams/$', edit_data_page),
    url(r'^add_matches/$', add_data_page),
    url(r'^remove_matches/$', remove_data_page),
    url(r'^edit_matches/$', edit_data_page),
    url(r'^add_bans/$', add_data_page),
    url(r'^remove_bans/$', remove_data_page),
    url(r'^add_competes/$', add_data_page),
    url(r'^remove_competes/$', remove_data_page),
    url(r'^edit_competes/$', edit_data_page),
    url(r'^add_interacts/$', add_data_page),
    url(r'^remove_interacts/$', remove_data_page),
    url(r'^edit_interacts/$', edit_data_page),
    url(r'^add_participates/$', add_data_page),
    url(r'^remove_participates/$', remove_data_page),
    url(r'^edit_participates/$', edit_data_page),
    url(r'^add_plays/$', add_data_page),
    url(r'^remove_plays/$', remove_data_page),
    url(r'^edit_plays/$', edit_data_page),
    url(r'^add_registers/$', add_data_page),
    url(r'^remove_registers/$', remove_data_page),
    url(r'^edit_registers/$', edit_data_page),
    url(r'^add_scores/$', add_data_page),
    url(r'^remove_scores/$', remove_data_page),
    url(r'^edit_scores/$', edit_data_page),
    url(r'^add_organizes/$', add_data_page),
    url(r'^remove_organizes/$', remove_data_page),
    url(r'^edit_organizes/$', edit_data_page),
]

# Cannot edit bans because all attributes are part of the primary key