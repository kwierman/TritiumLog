from django.contrib import admin

# Register your models here.
from logbooks.models import Logbook,LogDocument, LogEntry

class LogInline(admin.TabularInline):#or, admin.TabularInline
    model = LogDocument
    extra = 3

class LogbookAdmin(admin.ModelAdmin):
    #fields = ['name', 'start_date']
    list_display=('name','date_created')#, 'is_recent'
    list_filter = ['name']
    search_fields = ['name']
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['date_created'], 'classes': ['collapse']}),
    ]
    inlines = [LogInline]

class LogAdmin(admin.ModelAdmin):
    fields = ['title', 'start_time','log_book']
    list_display=['title']
    list_filter = ['title']
    search_fields = ['title']

class LogEntryAdmin(admin.ModelAdmin):
    fields=['log_doc','version','text']
    list_display=['version']
    list_filter=['version']
    search_fields=['log_doc']

admin.site.register(Logbook, LogbookAdmin)
admin.site.register(LogDocument, LogAdmin)
admin.site.register(LogEntry, LogEntryAdmin)