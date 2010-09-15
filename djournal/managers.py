'''Managers for Djournal.'''

from django.db import models

class PublicEntryManager(models.Manager):
    def get_query_set(self):
        query_set = super(PublicEntryManager, self).get_query_set()
        return query_set.filter(status__exact=self.model.PUBLIC_ENTRY_STATUS)

class PrivateEntryManager(models.Manager):
    def get_query_set(self):
        query_set = super(PrivateEntryManager, self).get_query_set()
        return query_set.filter(status__exact=self.model.PRIVATE_ENTRY_STATUS)

class DraftEntryManager(models.Manager):
    def get_query_set(self):
        query_set = super(DraftEntryManager, self).get_query_set()
        return query_set.filter(status__exact=self.model.DRAFT_ENTRY_STATUS)
