from .models import Task

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class TaskCreateView(CreateView):
    model = Task
    fields = ['text', 'day', 'reminder']
    SuccessMessageMixin.success_message = "Task Saved"
