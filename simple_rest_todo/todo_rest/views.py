from rest_framework import generics
from .models import TaskToDo
from .serializers import TaskSerializer


class TaskCreateView(
    generics.CreateAPIView
):  # "Create" operation (C) - It handles the POST request !
    queryset = TaskToDo.objects.all()
    serializer_class = TaskSerializer


class TaskListView(
    generics.ListAPIView
):  # Read operation (R) - It handles the GET request !
    queryset = TaskToDo.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(
    generics.UpdateAPIView
):  # "Update" operation (U) - It handles the PUT and PATCH requests !
    queryset = TaskToDo.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyView(
    generics.DestroyAPIView
):  # "Delete/Destroy" operation (D) -  It handles the DELETE request !
    queryset = TaskToDo.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveView(
    generics.RetrieveAPIView
):  # "Read" operation (R) for a SINGLE ENTITY - handles GET again !!!
    queryset = TaskToDo.objects.all()
    serializer_class = TaskSerializer
