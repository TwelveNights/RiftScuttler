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
        # url(r'^add_(?P<table_name>[\w])$', add_data_page, name='add-data'),
        # url(r'^remove_(?P<table_name>[\w])$', remove_data_page, name='remove-data'),
        # url(r'^edit_(?P<table_name>[\w])$', edit_data_page, name='edit-data'),
        # url(r'^view_(?P<table_name>[\w])$', view_data_page, name='view-data'),
]

url_nav_list = get_nav_list_raw()
urlpatterns_add = [url(r'^add_'+table_name+'/$', add_data_page, name='add-'+table_name) for i, table_name in enumerate(url_nav_list)]
urlpatterns_remove = [url(r'^remove_' + table_name + '/$', remove_data_page, name='remove-' + table_name) for i, table_name in enumerate(url_nav_list)]
urlpatterns_edit = [url(r'^edit_' + table_name + '/$', edit_data_page, name='edit-' + table_name) for i, table_name in enumerate(url_nav_list)]
urlpatterns_view = [url(r'^view_' + table_name + '/$', view_data_page, name='view-' + table_name) for i, table_name in enumerate(url_nav_list)]

urlpatterns.extend(urlpatterns_add)
urlpatterns.extend(urlpatterns_remove)
urlpatterns.extend(urlpatterns_edit)
urlpatterns.extend(urlpatterns_view)


"""
urlpatterns = [
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
    url(r'^edit_bans/$', edit_data_page, name='edit-bans'),
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
    # url(r'^add_wins/$', add_data_page, name='add-wins'),
    # url(r'^remove_wins/$', remove_data_page, name='remove-wins'),
    # url(r'^edit_wins/$', edit_data_page, name='edit-wins'),

    url(r'^view_tournaments/$', view_data_page, name='view-tournaments'),
    url(r'^view_series/$', view_data_page, name='view-series'),
    url(r'^view_champions/$', view_data_page, name='view-champions'),
    url(r'^view_items/$', view_data_page, name='view-items'),
    url(r'^view_players/$', view_data_page, name='view-players'),
    url(r'^view_teams/$', view_data_page, name='view-teams'),
    url(r'^view_matches/$', view_data_page, name='view-matches'),
    url(r'^view_bans/$', view_data_page, name='view-bans'),
    url(r'^view_competes/$', view_data_page, name='view-competes'),
    url(r'^view_interacts/$', view_data_page, name='view-interacts'),
    url(r'^view_participates/$', view_data_page, name='view-participates'),
    url(r'^view_plays/$', view_data_page, name='view-plays'),
    url(r'^view_registers/$', view_data_page, name='view-registers'),
    url(r'^view_scores/$', view_data_page, name='view-scores'),
    url(r'^view_organizes/$', view_data_page, name='view-organizes'),
    url(r'^view_wins/$', view_data_page, name='view-wins'),
]

"""

