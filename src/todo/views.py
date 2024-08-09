from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from todo.serializers import TaskSerializer, ListSerializer, TaskCreateSerializer
from todo.models import Task, List


class ListCreateView(CreateAPIView):
    model = List
    serializer_class = ListSerializer


class TaskViewSet(ModelViewSet):
    model = Task
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by("-created_date")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskCreateSerializer
        return TaskSerializer
