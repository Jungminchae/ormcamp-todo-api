from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TaskViewSet, ListCreateView


router = DefaultRouter()

router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls), name="tasks"),
    path("lists/", ListCreateView.as_view(), name="list-create"),
]
