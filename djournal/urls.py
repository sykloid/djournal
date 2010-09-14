'''URLs for Djournal.'''

from django.conf.urls.defaults import *

from djournal.models import Entry

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.date_based.archive_index',
        kwargs={
            'date_field': 'created',
            'num_latest': Entry.public.count(),
            'queryset': Entry.public.all(),
            'template_name': 'djournal/entry_index.html',
            'template_object_name': 'entries',
        },
        name='djournal_entry_index',
    ),
)
