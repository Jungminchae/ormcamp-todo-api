from django.urls import path
from todo.apis import api

urlpatterns = [path("", api.urls)]
