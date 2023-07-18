from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskRetrieveView,
    TaskUpdateView,
    TaskDestroyView,
)

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskRetrieveView.as_view(), name="task-retrieve"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDestroyView.as_view(), name="task-delete"),
]
