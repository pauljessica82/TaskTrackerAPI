from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from tasktrackerapi.api.urls import router

from tasks.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('tasks/', include('tasks.urls')),
    path('', index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]
