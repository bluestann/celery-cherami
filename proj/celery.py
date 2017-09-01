from __future__ import absolute_import, unicode_literals
from celery import Celery

from proj.consumer import consumer
from proj.publisher import publisher

app = Celery('proj',
             broker='cherami://',  # redis://localhost:6379/0'
            include=['proj.tasks'],
             cherami_publisher=publisher,
             cherami_consumer=consumer,)

app.conf.update(task_acks_late=True, worker_prefetch_multiplier=10)

if __name__ == '__main__':
    app.start()