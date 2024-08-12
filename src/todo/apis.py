from typing import List
from ninja import NinjaAPI
from todo.services import TaskService
from todo.schemas import TaskResponse

api = NinjaAPI()


@api.get("/todos", response=List[TaskResponse])
def get_todoes(request):
    task_service = TaskService()
    tasks = task_service.get_tasks()
    return list(tasks)
