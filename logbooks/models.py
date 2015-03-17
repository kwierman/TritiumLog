import datetime

from django.db import models
from django.utils import timezone


class Logbook(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date_created')
    """
    def is_recent(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.date_created <= now

    is_recent.admin_order_field = 'date_created'
    is_recent.boolean=True
    is_recent.short_description = 'Created Recently?'
    """
    def __unicode__(self):
        return self.name


class LogDocument(models.Model):
    log_book = models.ForeignKey(Logbook)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    start_time = models.DateTimeField('start_time')
    last_modified = models.DateTimeField('last modified')
    def __unicode__(self):
        return self.title


class LogEntry(models.Model):
    log_doc = models.ForeignKey(LogDocument)
    version = models.PositiveIntegerField()
    text = models.TextField()
    def __unicode__(self):
        return str(version)