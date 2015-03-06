from django.contrib import admin

# Register your models here.
from logbook.models import Logbook,Log


class LogInline(admin.StackedInline):#or, admin.TabularInline
    model = Log
    extra = 3

class LogbookAdmin(admin.ModelAdmin):
    #fields = ['name', 'start_date']
    list_display=('name','start_date', 'was_published_recently')
    list_filter = ['name']
    search_fields = ['name']
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['start_date'], 'classes': ['collapse']}),
    ]
    inlines = [LogInline]
class LogAdmin(admin.ModelAdmin):
    fields = ['title', 'start_date','log_book']
    list_display=['title']
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Logbook, LogbookAdmin)
admin.site.register(Log, LogAdmin)