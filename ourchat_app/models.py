from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):

    name = models.CharField(max_length=255)
    datetime_created = models.DateTimeField(auto_now_add=True)


class Message(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE, null=True)


class ChatRole(models.Model):

    ROLE_CREATOR = 16
    ROLE_MEMBER = 1
    ROLES = [
        [ROLE_CREATOR, "Создатель чата"],
        [ROLE_MEMBER, "Участник чата"]
    ]

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLES, default=ROLE_CREATOR)