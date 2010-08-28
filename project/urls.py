from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os

from django.conf import settings

from journals.views import *

site_media = os.path.join( os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    
    (r'^$', main),
    (r'^journals$', main),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media,'show_indexes': True}),
)

