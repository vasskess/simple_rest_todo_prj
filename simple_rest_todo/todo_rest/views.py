from rest_framework import generics

from .models import TaskToDo
from .serializers import TaskSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(responses=TaskSerializer)
class BasicTaskView(generics.GenericAPIView):
    queryset = TaskToDo.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(
    BasicTaskView, generics.CreateAPIView
):  # "Create" operation (C) - It handles the POST request !
    pass


class TaskListView(
    BasicTaskView, generics.ListAPIView
):  # Read operation (R) - It handles the GET request !
    pass


class TaskUpdateView(
    BasicTaskView, generics.UpdateAPIView
):  # "Update" operation (U) - It handles the PUT and PATCH requests !
    pass


class TaskDestroyView(
    BasicTaskView, generics.DestroyAPIView
):  # "Delete/Destroy" operation (D) -  It handles the DELETE request !
    pass


class TaskRetrieveView(
    BasicTaskView, generics.RetrieveAPIView
):  # "Read" operation (R) for a SINGLE ENTITY - handles GET again !!!
    pass
