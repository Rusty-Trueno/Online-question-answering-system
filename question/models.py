from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ques(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=50)
    quename=models.CharField(max_length=30)
    #num=models.CharField(max_length=10)

