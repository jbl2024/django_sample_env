from django.conf.urls.defaults import *

urlpatterns = patterns('sample.views',
    url(r'^dummy$', "dummy", name='sample_dummy'),
)
