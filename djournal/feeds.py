'''Feeds for Djournal.'''

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template

from taggit.models import Tag

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

class TaggedEntryFeed(Feed):
    def get_object(self, request, slug):
        return get_object_or_404(Tag, slug=slug)

    def items(self, obj):
        return Entry.public.filter(tags__in=[obj])

    def title(self, obj):
        template = get_template('djournal/feeds/tagged_entry_feed_title.html')
        return template.render(Context({'tag': obj}))

    def description(self, obj):
        template = get_template('djournal/feeds/tagged_entry_feed_description.html')
        return template.render(Context({'tag': obj}))

    def link(self, obj):
        return reverse('djournal_tagged_entry_index', kwargs={'slug': obj.slug})

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser_html

    def item_link(self, item):
        return item.get_absolute_url()
