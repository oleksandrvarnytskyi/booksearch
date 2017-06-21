from django.http import HttpResponseBadRequest
from django.shortcuts import render

from books.forms import RequestForm
from books.tasks import process_query


def bad_request(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request, '400.html', values_for_template, status=400)


def search_handler(request):
    """Function for search handling. It provides email validation and
    launching asynchronous celery tasks in case of receiving GET request."""
    if request.POST:
        # Put POST request into form
        form = RequestForm(request.POST)
        if form.is_valid():
            q = request.POST.get('q')
            email = request.POST.get('email')
            # launch celery task
            process_query.delay(q, email)
            return render(
                request,
                'books/processing_started.html',
                {'email': email}
            )
        return HttpResponseBadRequest()
    form = RequestForm()
    return render(request, 'main.html', {'form': form})
