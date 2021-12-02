from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    HiddenField,
    CharField,
    CurrentUserDefault
)
from tasks.models import Task


class TaskSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name="task-detail")

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'day',
            'reminder',
            'url',
        ]
