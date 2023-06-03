from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    username = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

# Create your models here.