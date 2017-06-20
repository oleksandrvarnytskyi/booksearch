from __future__ import absolute_import
from booksearch.celery import app
import time


@app.task
def process_query(query, email):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
