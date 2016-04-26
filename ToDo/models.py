from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    completed_date = models.DateTimeField(
        blank=True, null=True)

    def complete(self):
        self.completed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
