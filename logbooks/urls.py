from django.conf.urls import  url

from logbooks import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<logbook_id>\d+)/$', views.log_book_detail, name='log_book_detail'),
    url(r'^(?P<logbook_id>\d+)/(?P<logdocument_id>\d+)/$', views.log_document_detail, name='log_document_detail'),
    url(r'^(?P<logbook_id>\d+)/(?P<logdocument_id>\d+)/(?P<logentry_id>\d+)/$', views.log_entry_detail, name='log_entry_detail'),
]

