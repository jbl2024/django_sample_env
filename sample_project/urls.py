from django.conf.urls.defaults import *

import settings
from os import path as os_path

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^sample/', include('sample.urls')),
)


if settings.LOCAL_MODE:
    urlpatterns += patterns('',

    # if we are in local mode we need django to serve medias
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os_path.join(settings.PROJECT_PATH, 'media')}),

    )

