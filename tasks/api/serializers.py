from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    HiddenField,
    CharField,
    CurrentUserDefault,
    DateTimeField
)

from tasks.models import Task


class TaskSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name="task-detail")
    # day = DateTimeField()
    day = DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Task
        fields = [
            'id',
            'text',
            'day',
            'reminder',
            'url',
        ]
