import logging

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from django.template import RequestContext, loader

from logbooks.models import Logbook, LogDocument, LogEntry

from django.views import generic

from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

"""
class IndexView(generic.ListView):
    template_name = 'logbooks/index.html'
    context_object_name = 'latest_logbook_list'

    def get_queryset(self):
        
        return Logbook.objects.order_by('-name')[:5]

class DetailView(generic.DetailView):
    model = Logbook
    template_name = 'logbooks/detail.html'

"""

@login_required
def index(request):
    latest_logbook_list = Logbook.objects.order_by('-name')[:5]
    logger.debug('The Latest List of logbooks: '+str(latest_logbook_list))
    context = {'latest_logbook_list': latest_logbook_list, 'SITENAME': "Logbook Viewer"}
    return render(request, 'logbooks/index.html', context)

@login_required
def log_book_detail(request, logbook_id):
    try:
        logbook = Logbook.objects.get(pk=logbook_id)
    except Logbook.DoesNotExist:
        raise Http404("Logbook does not exist")
    logs = LogDocument.objects.filter(log_book_id=logbook_id)
    return render(request, 'logbooks/log_book_detail.html', {'logbook': logbook, 'logs' : logs, 'SITENAME': "Log Viewer" })

@login_required
def log_document_detail(request, logbook_id, logdocument_id):
    try:
        logbook = Logbook.objects.get(pk=logbook_id)
        logdoc = LogDocument.objects.get(pk=logdocument_id)
    except Logbook.DoesNotExist, LogDocument.DoesNotExist:
        raise Http404("Logbook or LogDocument does not exist")
    log_entries = LogEntry.objects.filter(log_doc_id = logdocument_id)
    return HttpResponse("This is a log document Detail in logbook")

@login_required
def log_entry_detail(request, log_entry_id):
    return HttpResponse("This is a Log Entry Detail")
