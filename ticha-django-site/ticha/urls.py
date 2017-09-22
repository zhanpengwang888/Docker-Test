"""ticha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n'))
]

# the i18n_patterns() method strips the language prefix and adds it to the
# request object passed to each view as request.LANGUAGE_CODE
urlpatterns += i18n_patterns(
    # URLs for static pages
    url(r'^$', views.index, name='index'),
    url('^about/$', views.about, name='about'),
    url('^team/$', views.team, name='team'),
    url('^acknowledgements/$', views.acknowledgements, name='acknowledgements'),
    url('^linguistic/$', views.linguistic, name='linguistic'),
    url('^context/$', views.context, name='context'),
    url('^arte/$', views.arte, name='arte'),
    url('^sample_arte/$', views.sample_arte, name='sample_arte'),
    url('^doctrina/$', views.doctrina, name='doctrina'),
    url('^feria/$', views.feria, name='feria'),
    url('^sample_doctrina/$', views.sample_doctrina, name='sample_doctrina'),
    url('^handwritten/$', views.handwritten, name='handwritten'),
    url('^sample_handwritten/$', views.sample_handwritten, name='sample_handwritten'),
    url('^timeline/$', views.timeline, name='timeline'),
    url('^bibliography/$', views.bibliography, name='bibliography'),
    url('^arte_pdf/$', views.arte_pdf, name='arte_pdf'),
    url('^outline/levanto$', views.levanto_outline, name='levanto_outline'),
    url('^outline/arte$', views.arte_outline, name='arte_outline'),
    url('^arte_original/$', views.arte_original, name='arte_original'),
    url('^reg_spanish/$', views.reg_spanish, name='reg_spanish'),
    url('^doctrina_pdf/$', views.doctrina_pdf, name='doctrina_pdf'),
    url('^form/$', views.form, name='form'),
    url('^resources/$', views.resources, name='resources'),
    # handling "/index" url request
    url(r'^index/$', views.index, name='index'),
    # URLs from other apps
    url(r'^vocabulary/', include('vocabulary.urls')),
    url(r'^', include('zapotexts.urls')),
    url(r'^', include('handwritten_texts.urls')),
)
