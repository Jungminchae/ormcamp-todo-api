from rest_framework.generics import ListAPIView, CreateAPIView
from todo.serializers import TaskSerializer, ListSerializer
from todo.models import Task, List


class ListCreateView(CreateAPIView):
    model = List
    serializer_class = ListSerializer


class TaskListView(ListAPIView):
    model = Task
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by("-created_date")
