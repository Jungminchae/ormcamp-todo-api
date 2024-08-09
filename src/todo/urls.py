from django.urls import path
from todo.views import TaskListView, ListCreateView

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("lists/", ListCreateView.as_view(), name="list-create"),
]
