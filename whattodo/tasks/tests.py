from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

# Create your tests here.
class TaskAPITests(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description")

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

   

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)