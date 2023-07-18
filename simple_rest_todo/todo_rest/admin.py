from django.contrib import admin
from .models import TaskToDo


@admin.register(TaskToDo)
class TaskToDoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "completed",
    )
