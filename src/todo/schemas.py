from ninja import Schema
from datetime import datetime


class ListResponse(Schema):
    id: int
    name: str
    description: str


class TaskResponse(Schema):
    title: str
    description: str
    created_date: datetime
    due_date: datetime
    completed: bool
    list: ListResponse
    priority: int
