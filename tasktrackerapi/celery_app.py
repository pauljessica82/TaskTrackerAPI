import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasktrackerapi.settings')
app = Celery('tasktrackerapi', broker=settings.CELERY_BROKER_URL)
app.conf.timezone = 'America/New_York'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reminder-time': {
        'task': 'tasks.celery_tasks.send_reminder',
        'schedule': crontab(),
    }
}
