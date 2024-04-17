from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    projects = models.ManyToManyField('Project', related_name='workers')


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return "{owner}.{project}".format(project=self.name,
                                          owner=self.owner)


class Work(models.Model):
    worker = models.ForeignKey('User', related_name='worker')
    project = models.ForeignKey('Project', related_name='work_done')
    datetime = models.DateTimeField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return "{project} - {worker} {date} ({duration}min)".format(
            project=self.project, worker=self.worker,
            date=timezone.localtime(self.datetime), duration=self.duration)
