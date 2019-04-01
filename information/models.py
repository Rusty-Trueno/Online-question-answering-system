from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class info (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)