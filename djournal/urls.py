'''URLs for Djournal.'''

from django.conf.urls.defaults import *

from djournal.models import Entry

urlpatterns = patterns('',
    url(r'^$', 'djournal.views.entry_index',
        name='djournal_entry_index',
    ),
    url(r'^tag/(?P<slug>.*)/$', 'djournal.views.tagged_entry_index',
        name='djournal_tagged_entry_index',
    ),
    url(r'^(?P<slug>.*)/$', 'djournal.views.entry_detail',
        name='djournal_entry_detail',
    ),
)
