from todo.models import Task


class TaskService:
    def get_tasks(self):
        tasks = Task.objects.all()
        return tasks
