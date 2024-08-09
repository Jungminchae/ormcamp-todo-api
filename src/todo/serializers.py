from rest_framework import serializers
from .models import Task, List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    list = ListSerializer()

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = [
            "created_date",
        ]


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "list"]
