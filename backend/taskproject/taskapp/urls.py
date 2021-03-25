from django.urls import path, include
from .views import TasksAPIView, TaskAPIView, TaskCreateView

app_name = "taskapp"

urlpatterns = [
    path('tasks', TasksAPIView.as_view()),
    path('tasks/<int:pk>', TaskAPIView.as_view()),
    path('create', TaskCreateView.as_view()),
]
