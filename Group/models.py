from django.db import models


class Group(models.Model):
    creator = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='assign', default=User.objects.first())
    prize = models.IntegerField(validators=[MaxValueValidator(1000)])
    about = models.TextField()
    