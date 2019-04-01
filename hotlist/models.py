from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class hotques(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=50)
    quename=models.CharField(max_length=30)
    hotid = models.IntegerField()