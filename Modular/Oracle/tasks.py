from django.db import models
from .employees import Employee

class TaskStatus(models.Model):
    title = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, null=True)
    datestamp = models.DateTimeField(null=True)
    def __str__(self):
        return self.title

