from django.conf.urls import url, include

from . import views

app_name = 'handwritten_texts'


urlpatterns = [
    url(r'^texts/handwritten/$', views.HandwrittenListView.as_view(), name='list'),
    url(r'^texts/(?P<slug>[A-Za-z0-9]+)/$', views.handwritten_text_detail_view, name='detail'),
    # redirect from old URL
    url(r'^handwritten_texts.html/$', views.redirect_view, name='redirect'),
    url(r'^handwritten_texts/$', views.redirect_view, name='redirect'),
]
