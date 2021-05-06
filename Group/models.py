from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Group(models.Model):
    creator = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='maker', default=User.objects.first())
    prize = models.IntegerField(validators=[MaxValueValidator(1000)])
    about = models.TextField()
    