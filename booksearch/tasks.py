from __future__ import absolute_import

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from haystack.forms import SearchForm

from booksearch import settings
from booksearch.celery import app


@app.task
def process_query(get_obj, email):
    """Function for processing of a request and sending email with results
    using celery"""
    print('task begins')
    form = SearchForm(get_obj)
    # Launch searching
    books = form.search()
    # sending email with results
    query = get_obj.get('q')
    subject = 'Results of books searching'
    html_content = render_to_string(
        'books/results_email.html',
        {
            'query': query,
            'books': books,
        }
    )
    text_content = strip_tags(html_content)
    send_mail(
        subject,
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=True,
        html_message=html_content
    )
    print('task finished')
