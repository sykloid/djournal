'''Admin specification for Djournal.'''

from django.contrib import admin

from djournal.models import Entry

class EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
