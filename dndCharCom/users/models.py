from django.db import models
from django.contrib.auth.models import AbstractUser

#using the built in Django User functionality, we only need to add additional fields
class User(AbstractUser):
    security_question = models.CharField(max_length=200, null=True, blank=True)
    security_answer = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
