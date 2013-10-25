from django.conf.urls import patterns, include, url
import ChiChi.views
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChiChiDjango.views.home', name='home'),
    # url(r'^ChiChiDjango/', include('ChiChiDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
    url(r'^hello/$', ChiChi.views.hello),
    url(r'^$', ChiChi.views.index),
    url(r'^about/$', ChiChi.views.about),
    url(r'^result/$', ChiChi.views.submit_comment),
)
