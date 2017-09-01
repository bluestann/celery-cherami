from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task(bind=True, max_retries=None)
def xsum(self, numbers):
    try:
        return sum(numbers)
    except Exception:
        self.retry(countdown=30 * 60)

