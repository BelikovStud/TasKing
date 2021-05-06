from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Group(models.Model):
    name = models.CharField(max_length=20, default="NoName")
    creator = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='maker')
    prize = models.IntegerField(validators=[MaxValueValidator(1000)])
    about = models.TextField(blank=True)
    