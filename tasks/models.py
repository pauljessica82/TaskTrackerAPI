from django.db import models
from django.conf import settings
from twilio.rest import Client
from datetime import datetime


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    day = models.DateTimeField()
    reminder = models.BooleanField(default=True)

    #   if self.reminder and self.day (NOW) is equal to datetime , then .....send message
    def send_reminder_text(self):
        client = (Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
        now = datetime.now()
        if self.reminder:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Reminder is Active',
                to='whatsapp:+19544009256'
            )
            print(message.sid)

    def save(self, *args, **kwargs):
        self.send_reminder_text()
        super(Task, self).save(*args, **kwargs)
