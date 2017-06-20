from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response
from django.core.validators import validate_email

from haystack.forms import SearchForm

from booksearch.tasks import process_query


def search_handler(request):
    if request.GET:
        # q = request.GET.get('q')
        form = SearchForm(request.GET)
        notes = form.search()
        email = request.GET.get('email')
        # try:
        #     validate_email(email)
        # except ValidationError:
        #     return render(request, 'main.html')
        return render_to_response('main.html', {'notes': notes})
        # process_query.daley(form, email)
        # return render(
        #     request,
        #     'books/processing_started.html',
        #     {'email': email}
        # )
    return render(request, 'main.html')
