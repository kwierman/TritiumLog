from django.db import models

from django.utils import timezone
import datetime

# Create your models here.

class Logbook(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')

    def was_published_recently(self):
        now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.start_date <= now
    was_published_recently.admin_order_field = 'start_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Log(models.Model):
    log_book = models.ForeignKey(Logbook)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    start_time = models.DateTimeField('start_time')
    last_modified = models.DateTimeField('last modified')

    # email_responsible = models.EmailField(max_length=75)
    # log_file =  models.FileField(upload_to='documents/%Y/%m/%d')
    # image field ImageField(upload_to='documents/%Y/%m/%d')


