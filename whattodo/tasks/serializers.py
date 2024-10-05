from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_due_date(self, value):
        """Ensure that the due date is not in the past."""
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def create(self, validated_data):
        """Override create method to handle additional logic if needed."""
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Override update method to handle additional logic if needed."""
        return super().update(instance, validated_data)