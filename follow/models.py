from django.db import models

# Create your models here.
class follow(models.Model):
    user=models.CharField(max_length=30)
    follower=models.CharField(max_length=30)