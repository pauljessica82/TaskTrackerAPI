from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from tasktrackerapi.api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('tasks/', include('tasks.urls')),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]
