from django.db import models
from django.conf import settings


# {
#     "id": 2,
#     "text": "Meeting at School",
#     "day": "Feb 6th at 1:30pm",
#     "reminder": false
# },

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    day = models.DateField()
    reminder = models.BooleanField(default=True)
