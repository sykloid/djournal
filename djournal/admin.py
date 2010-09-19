'''Admin specification for Djournal.'''

from datetime import datetime

from django.contrib import admin

from djournal.models import Entry

class EntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'

    exclude = ('author', 'created', 'modified')

    fieldsets = (
        ('Meta', {
            'fields': ('title', 'subtitle', 'slug', 'status', 'tags'),
        }),
        ('Content', {
            'fields': ('teaser', 'body'),
        }),
    )

    list_display = (
        'title', 'subtitle', 'slug', 'author', 'created', 'modified', 'status',
    )

    list_filter = (
        'author',
        'status',
    )

    prepopulated_fields = {
        'slug': ('title',),
    }

    search_fields = (
        'title', 'subtitle', 'slug', 'body', 'teaser',
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.created = datetime.now()

        obj.modified = datetime.now()

        obj.save()

admin.site.register(Entry, EntryAdmin)
