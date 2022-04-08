from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
