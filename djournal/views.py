'''Views for Djournal.'''

from django.shortcuts import render_to_response
from django.template import RequestContext

from djournal.models import Entry

def entry_index(request, limit=0, template='djournal/entry_index.html'):
    '''Returns a reponse of a fixed number of entries; all of them, by default. '''

    entries = Entry.public.all()

    if limit > 0:
        entries = entries[:limit]

    context = {
        'entries': entries,
    }

    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request),
    )
