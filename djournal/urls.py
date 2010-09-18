'''URLs for Djournal.'''

from django.conf.urls.defaults import *

from djournal.models import Entry

urlpatterns = patterns('',
    url(r'^$', 'djournal.views.entry_index',
        name='djournal_entry_index',
    ),
    url(r'^(?P<slug>.*)/$',
        'django.views.generic.list_detail.object_detail',
        kwargs={
            'queryset': Entry.public.all(),
            'slug_field': 'slug',
            'template_name': 'djournal/entry_detail.html',
            'template_object_name': 'entry',
        },
        name='djournal_entry_detail',
    ),
)
