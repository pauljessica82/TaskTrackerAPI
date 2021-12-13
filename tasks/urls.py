from django.urls import path
from django.contrib import admin


from tasks.views import TaskCreateView

app_name = 'tasks'

urlpatterns = [
    path("create", TaskCreateView.as_view()),
]
