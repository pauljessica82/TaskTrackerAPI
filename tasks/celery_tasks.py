import string
import datetime
import sqlite3

from django.conf import settings

from twilio.rest import Client

from sqlite3 import Error

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task
def send_reminder():
    # if self.reminder and self.day (NOW) is equal to datetime , then .....send message
    def send_reminder_text(self):
        client = (Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
        now = datetime.now().replace(second=0, microsecond=0)
        while 1 == 1:
            if self.day == now:
                if self.reminder:
                    message = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body='Reminder is Active',
                        to='whatsapp:+19544009256'
                    )
                    print(message.sid)
            break
