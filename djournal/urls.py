'''URLs for Djournal.'''

from django.conf.urls.defaults import *

from djournal.feeds import EntryFeed, TaggedEntryFeed
from djournal.models import Entry
from djournal.sitemaps import EntrySitemap

urlpatterns = patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'entry': EntrySitemap}},
    ),
    url(r'^$', 'djournal.views.entry_index',
        name='djournal_entry_index',
    ),
    url(r'^feed/$', EntryFeed(),
        name='djournal_entry_feed'
    ),
    url(r'^tag/(?P<slug>.*)/feed/$', TaggedEntryFeed(),
        name='djournal_tagged_entry_feed',
    ),
    url(r'^tag/(?P<slug>.*)/$', 'djournal.views.tagged_entry_index',
        name='djournal_tagged_entry_index',
    ),
    url(r'^(?P<slug>.*)/$', 'djournal.views.entry_detail',
        name='djournal_entry_detail',
    ),
)
