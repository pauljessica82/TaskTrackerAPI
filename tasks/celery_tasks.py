import logging

from tasks.models import Task

from twilio.rest import Client

from django.utils import timezone
from django.conf import settings

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def send_reminder():
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    tasks = (Task.objects.filter(reminder=1))

    client = Client(account_sid, auth_token)
    for t in tasks:

        now = timezone.now().astimezone().replace(microsecond=0, second=0)
        reminder_time = t.day.astimezone().replace(microsecond=0, second=0)

        if now == reminder_time:
            message = client.messages.create(
                from_=settings.TWILIO_NUMBER,
                body=t.text,
                to=settings.TWILIO_MY_PHONE
            )
            print(message.sid)
            logger.info("TASK SENT")
