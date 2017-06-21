from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.core.validators import validate_email

from booksearch.tasks import process_query


def search_handler(request):
    """Function for search handling. It provides email validation and
    launching asynchronous celery tasks in case of receiving GET request."""
    if request.GET:
        get_obj = request.GET
        email = request.GET.get('email')
        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'main.html', {'flag': True})
        # launch celery task
        process_query.delay(get_obj, email)
        return render(
            request,
            'books/processing_started.html',
            {'email': email}
        )
    return render(request, 'main.html')
