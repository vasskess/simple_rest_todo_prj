from rest_framework import serializers

from simple_rest_todo.todo_rest.models import TaskToDo


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskToDo
        fields = "__all__"
