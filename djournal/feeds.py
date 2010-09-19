'''Feeds for Djournal.'''

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template

from djournal.models import Entry

class EntryFeed(Feed):
    def title(self):
        template = get_template('djournal/feeds/entry_feed_title.html')
        return template.render(Context({}))

    def description(self):
        template = get_template('djournal/feeds/entry_feed_description.html')
        return template.render(Context({}))

    def link(self):
        return reverse('djournal_entry_index')

    def items(self):
        return Entry.public.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser_html

    def item_link(self, item):
        return item.get_absolute_url()
