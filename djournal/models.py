'''Models for Djournal.'''

from django.contrib.auth.models import User
from django.db import models

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

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

        get_latest_by = 'created'
        ordering = ('-created',)
