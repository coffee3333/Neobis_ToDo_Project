from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=16)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title