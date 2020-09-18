import datetime
import time
import logging
from celery import Celery
from flask import current_app

logger = logging.getLogger()
celery = Celery(__name__, autofinalize=False)

@celery.task(bind=True)
def wait_task(self, sleep_time):
    '''sample task that sleeps 5 seconds then returns the current datetime'''
    unleash = current_app.extensions['Unleash']
    print(f"Unleash Worker check: {unleash.client.is_enabled('ivantest')}")

    time.sleep(sleep_time)
    return datetime.datetime.now().isoformat()
