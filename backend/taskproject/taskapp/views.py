from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

class TasksAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()