'''Admin specification for Djournal.'''

from datetime import datetime

from django.contrib import admin

from djournal.models import Entry

class EntryAdmin(admin.ModelAdmin):
    exclude = ('author', 'created', 'modified')

    fieldsets = (
        ('Meta', {
            'fields': ('title', 'subtitle', 'slug'),
        }),
        ('Content', {
            'fields': ('teaser', 'body'),
        }),
    )

    list_display = (
        'title', 'subtitle', 'slug', 'author', 'created', 'modified',
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.created = datetime.now()

        obj.modified = datetime.now()

        obj.save()

admin.site.register(Entry, EntryAdmin)
