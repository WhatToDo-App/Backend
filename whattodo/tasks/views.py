from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the WhatToDo App!</h1><p><a href='/api/tasks/'>View Tasks</a></p>")