from .models import Task
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class TaskCreateView(CreateView):
    model = Task
    fields = ['text', 'day', 'reminder']
    SuccessMessageMixin.success_message = "Task Saved"

# Serve react frontend page
index = TemplateView.as_view(template_name='index.html')


