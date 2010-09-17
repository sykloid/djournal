'''Models for Djournal.'''

from django.contrib.auth.models import User
from django.db import models

from djournal import managers

try:
    from ripwrap.core import formatter
except ImportError:
    formatter = lambda text: text

class Entry(models.Model):
    '''Represents a Djournal entry.'''

    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True)

    slug = models.SlugField(max_length=128, unique=True)

    author = models.ForeignKey(User, related_name='entries')

    created = models.DateTimeField()
    modified = models.DateTimeField()

    teaser = models.TextField(blank=True)
    body = models.TextField(blank=True)

    teaser_html = models.TextField(blank=True, editable=False)
    body_html = models.TextField(blank=True, editable=False)

    PUBLIC_ENTRY_STATUS = 'public'
    PRIVATE_ENTRY_STATUS = 'private'
    DRAFT_ENTRY_STATUS = 'draft'

    ENTRY_STATUSES = (
        (PUBLIC_ENTRY_STATUS, 'Public'),
        (PRIVATE_ENTRY_STATUS, 'Private'),
        (DRAFT_ENTRY_STATUS, 'Draft'),
    )

    status = models.CharField(
        max_length=16,
        choices=ENTRY_STATUSES,
        default=PUBLIC_ENTRY_STATUS
    )

    objects = models.Manager()
    public = managers.PublicEntryManager()
    private = managers.PrivateEntryManager()
    draft = managers.DraftEntryManager()

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

        get_latest_by = 'created'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.teaser_html = formatter.render(self.teaser)
        self.body_html = formatter.render(self.body)

        super(Entry, self).save()
