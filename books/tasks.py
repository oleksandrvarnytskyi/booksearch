from __future__ import absolute_import

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from haystack.forms import SearchForm

from booksearch import settings
from booksearch.celery import app


@app.task
def process_query(query, email):
    """Function for processing of a request and sending email with results
    using celery"""
    form = SearchForm({'q': query})
    # Launch searching
    books = form.search()
    # sending email with results
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
