from django.db import models


class TaskToDo(models.Model):
    TITLE_MAX_LEN = 200
    DESC_MAX_LEN = 2000

    title = models.CharField(max_length=TITLE_MAX_LEN)
    description = models.TextField(max_length=DESC_MAX_LEN)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ToDo Tasks"
