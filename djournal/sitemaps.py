'''Sitemaps for Djournal.'''

from django.contrib.sitemaps import Sitemap

from djournal.models import Entry

class EntrySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Entry.public.all()

    def lastmod(self, obj):
        return obj.modified
