from django.conf.urls import url

from . import views

app_name = 'vocabulary'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reverse_index/$', views.reverse_index, name='reverse_index'),
    url(r'^(?P<letter>[\w]+)/$', views.index, name='index'),
]
