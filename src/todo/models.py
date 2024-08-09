from django.db import models
from django.utils.translation import gettext_lazy as _


class List(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("이름"))
    description = models.TextField(blank=True, verbose_name=_("설명"))

    def __str__(self):
        return self.name


class Task(models.Model):
    class PriorityChoices(models.IntegerChoices):
        LOW = 1, _("낮음")
        MEDIUM = 2, _("중간")
        HIGH = 3, _("높음")

    title = models.CharField(max_length=200, verbose_name=_("제목"))
    description = models.TextField(blank=True, verbose_name=_("설명"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("생성일"))
    due_date = models.DateTimeField(null=True, blank=True, verbose_name=_("마감일"))
    completed = models.BooleanField(default=False, verbose_name=_("완료"))
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
        verbose_name=_("리스트"),
    )
    priority = models.IntegerField(
        choices=PriorityChoices.choices,
        default=PriorityChoices.MEDIUM,
        verbose_name=_("우선순위"),
    )

    def __str__(self):
        return f"{self.title} (우선순위: {self.get_priority_display()})"
