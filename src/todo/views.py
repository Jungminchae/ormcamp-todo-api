from rest_framework.generics import ListAPIView
from todo.serializers import TaskSerializer
from todo.models import Task


class TaskListView(ListAPIView):
    model = Task
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by("-created_date")
