from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Task(models.Model):
    assignee = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='assign', default=User.objects.first())
    title = models.CharField(max_length=15)
    description = models.TextField()
    points = models.IntegerField(validators=[MaxValueValidator(10)])
