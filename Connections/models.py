from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils import timezone
from Group.models import Group
from Task.models import Task

class GroupTaskConnection(models.Model):
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='grp')
    task = models.ForeignKey(Task, on_delete=models.RESTRICT, related_name='tsk')
    date_added = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_all_tasks_of_group(cls, group):
        return cls.objects.filter(group=group)


class GroupUserConnection(models.Model):
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='grpc')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='usr')
    score = models.IntegerField(validators=[MaxValueValidator(1000)])

    @classmethod
    def get_all_groups_of_user(cls, user):
        return cls.objects.filter(user=user)
