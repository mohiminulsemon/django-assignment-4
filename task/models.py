from django.db import models
# from category.models import TaskCategory

# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_Assign_Date = models.DateField()
    # categories = models.ForeignKey(TaskCategory)

    def __str__(self):
        return self.taskTitle