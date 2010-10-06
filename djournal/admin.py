'''Admin specification for Djournal.'''

from datetime import datetime

from django.contrib import admin

from djournal.models import Entry

class EntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'

    exclude = ('author',)

    fieldsets = (
        ('Meta', {
            'fields': ('title', 'subtitle', 'slug', 'status', 'tags',
                       'created', 'modified'),
        }),
        ('Content', {
            'fields': ('teaser', 'body'),
        }),
    )

    list_display = (
        'title', 'subtitle', 'slug_link', 'author',
        'format_created', 'format_modified', 'status',
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

        obj.save()

    def slug_link(self, obj):
        return '<a href="{url}">{slug}</a>'.format(
            url=obj.get_absolute_url(), 
            slug=obj.slug
        )

    slug_link.allow_tags = True
    slug_link.short_description = 'Slug'

    def format_created(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M")
    format_created.short_description = 'Created'

    def format_modified(self, obj):
        return obj.modified.strftime("%Y-%m-%d %H:%M")
    format_modified.short_description = 'Modified'

admin.site.register(Entry, EntryAdmin)
