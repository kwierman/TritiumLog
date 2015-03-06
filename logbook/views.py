from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from django.template import RequestContext, loader

from logbook.models import Logbook, Log

from django.views import generic


class IndexView(generic.ListView):
    template_name = 'logbook/index.html'
    context_object_name = 'latest_logbook_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Logbook.objects.order_by('-name')[:5]


class DetailView(generic.DetailView):
    model = Logbook
    template_name = 'logbook/detail.html'


class ResultsView(generic.DetailView):
    model = Logbook
    template_name = 'logbook/results.html'



def index(request):
    latest_logbook_list = Logbook.objects.order_by('-name')[:5]
    context = {'latest_logbook_list': latest_logbook_list}
    return render(request, 'logbook/index.html', context)

def detail(request, question_id):
    try:
        logbook = Logbook.objects.get(pk=question_id)
    except LogBook.DoesNotExist:
        raise Http404("Logbook does not exist")
    return render(request, 'logbook/detail.html', {'logbook': logbook})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def log(request, question_id):
    p = get_object_or_404(Logbook, pk=question_id)
    try:
        selected_choice = p.log_set.get(pk=request.POST['log'])
    except (KeyError, Log.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'logbook/detail.html', {
            'log': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        log.votes += 1
        log.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('logbook:results', args=(p.id,)))

def results(request, logbook_id):
    logbook = get_object_or_404(Logbook, pk=logbook_id)
    return render(request, 'polls/results.html', {'logbook': logbook})