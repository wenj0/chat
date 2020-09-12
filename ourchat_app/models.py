from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)