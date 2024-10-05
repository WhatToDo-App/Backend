from rest_framework import generics, viewsets
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def perform_create(self, serializer):
        # Save the task with the currently authenticated user
        serializer.save(user=self.request.user)

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Optional if you want to enforce this here too

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Optional

def home(request):
    return HttpResponse("<h1>Welcome to the WhatToDo App!</h1><p><a href='/api/tasks/'>View Tasks</a></p>")
