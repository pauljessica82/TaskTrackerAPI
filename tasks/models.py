from django.db import models
from django.conf import settings


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    day = models.DateTimeField()
    reminder = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
