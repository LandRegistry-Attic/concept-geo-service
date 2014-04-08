from django.conf.urls import patterns, include, url
from titles.api import TitlesResource

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concept_geo_service.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^titles', include(TitlesResource.urls())),
    url(r'^titles/', include(TitlesResource.urls())),
    url(r'^titles-revisions', include(TitlesResource.urls()))

)
