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
    url(r'^$', curator_home, name='curator-home'),
    url(r'^logout/$', logout_view, name='logout-page'),
    url(r'^add_tournaments/$', add_data_page, name='add-tournaments'),
    url(r'^remove_tournaments/$', remove_data_page, name='remove-tournaments'),
    url(r'^edit_tournaments/$', edit_data_page, name='edit-tournaments'),
    url(r'^add_series/$', add_data_page, name='add-series'),
    url(r'^remove_series/$', remove_data_page, name='remove-series'),
    url(r'^edit_series/$', edit_data_page, name='edit-series'),
    url(r'^add_champions/$', add_data_page, name='add-champions'),
    url(r'^remove_champions/$', remove_data_page, name='remove-champions'),
    url(r'^edit_champions/$', edit_data_page, name='edit-champions'),
    url(r'^add_items/$', add_data_page, name='add-items'),
    url(r'^remove_items/$', remove_data_page, name='remove-items'),
    url(r'^edit_items/$', edit_data_page, name='edit-items'),
    url(r'^add_players/$', add_data_page, name='add-players'),
    url(r'^remove_players/$', remove_data_page, name='remove-players'),
    url(r'^edit_players/$', edit_data_page, name='edit-players'),
    url(r'^add_teams/$', add_data_page, name='add-teams'),
    url(r'^remove_teams/$', remove_data_page, name='remove-teams'),
    url(r'^edit_teams/$', edit_data_page, name='edit-teams'),
    url(r'^add_matches/$', add_data_page, name='add-matches'),
    url(r'^remove_matches/$', remove_data_page, name='remove-matches'),
    url(r'^edit_matches/$', edit_data_page, name='edit-matches'),
    url(r'^add_bans/$', add_data_page, name='add-bans'),
    url(r'^remove_bans/$', remove_data_page, name='remove-bans'),
    url(r'^add_competes/$', add_data_page, name='add-competes'),
    url(r'^remove_competes/$', remove_data_page, name='remove-competes'),
    url(r'^edit_competes/$', edit_data_page, name='edit-competes'),
    url(r'^add_interacts/$', add_data_page, name='add-interacts'),
    url(r'^remove_interacts/$', remove_data_page, name='remove-interacts'),
    url(r'^edit_interacts/$', edit_data_page, name='edit-interacts'),
    url(r'^add_participates/$', add_data_page, name='add-participates'),
    url(r'^remove_participates/$', remove_data_page, name='remove-participates'),
    url(r'^edit_participates/$', edit_data_page, name='edit-participates'),
    url(r'^add_plays/$', add_data_page, name='add-plays'),
    url(r'^remove_plays/$', remove_data_page, name='remove-plays'),
    url(r'^edit_plays/$', edit_data_page, name='edit-plays'),
    url(r'^add_registers/$', add_data_page, name='add-registers'),
    url(r'^remove_registers/$', remove_data_page, name='remove-registers'),
    url(r'^edit_registers/$', edit_data_page, name='edit-registers'),
    url(r'^add_scores/$', add_data_page, name='add-scores'),
    url(r'^remove_scores/$', remove_data_page, name='remove-scores'),
    url(r'^edit_scores/$', edit_data_page, name='edit-scores'),
    url(r'^add_organizes/$', add_data_page, name='add-organizes'),
    url(r'^remove_organizes/$', remove_data_page, name='remove-organizes'),
    url(r'^edit_organizes/$', edit_data_page, name='edit-organizes'),
]
