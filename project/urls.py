#!/usr/env python2.5

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os

from django.conf import settings

from journal.views import *


site_media = os.path.join( os.path.dirname(__file__), 'public')

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),   

    (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/site_media/favicon.ico'}),
    (r'^favicon\.gif$', 'django.views.generic.simple.redirect_to', {'url': '/site_media/favicon.gif'}),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),

    (r'^$', recent(size=None)),
    (r'^journal/recent$', 'django.views.generic.simple.redirect_to', {'url': '/journal/recent/100'}),
    (r'^journal/recent/(?P<size>\d+)/$', recent),
    
    (r'^journal/all$', all),
    (r'^journal$', all),
    (r'^journal/(?P<id>\d+)/$', view_with_id),

    #(r'^post/journal$', post),
)


