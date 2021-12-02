from django.shortcuts import get_object_or_404

from tasks.models import Task
from rest_framework.viewsets import ModelViewSet

from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
