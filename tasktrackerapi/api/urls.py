from rest_framework import routers
from tasks.api.views import TaskViewSet
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

