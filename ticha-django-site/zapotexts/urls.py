"""This module defines the URL patterns for the zapotexts app."""
from django.conf.urls import url, include

from . import views

app_name = 'zapotexts'


urlpatterns = [
    url(r'^texts/$', views.landing, name='landing'),
    # Levanto redirect
    url(r'^texts/levanto/$', views.levanto_redirect, name='levanto_redirect'),
    # Haystack search
    url(r'^search/?$', views.CustomSearchView.as_view(), name='search'),
    # Admin dictionary upload
    url(r'^admin/dictionary/$', views.AdminDictionary, name="admin_dictionary"),
    # Admin XML upload
    url(r'^admin/import_xml/$', views.admin_import_xml, name='import_xml'),
    url(r'^import_xml_post/$', views.admin_import_xml, name='import_xml_post'),
    # Document viewer views
    url(r'^texts/(?P<slug>[\w-]+)/viewer/$', views.document_viewer, name='document_viewer'),
    url(r'^texts/(?P<slug>[\w-]+)/viewer/(?P<page>[0-9]+)/$', views.document_viewer,
        name='document_viewer'),
]

# Page detail view (and download view)
modes = '(?P<mode>original|regular|english|workshop)'
page_pattern = r'^texts/(?P<slug>[\w-]+)/(?P<page>\d+)/' + modes + '/'
urlpatterns.append(url(page_pattern + '$', views.document_viewer, name='page_detail'))
urlpatterns.append(url(page_pattern + 'download/$', views.page_download_view, name='page_download'))
