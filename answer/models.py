from django.db import models
from django.contrib.auth.models import User
from question.models import ques
from ckeditor.fields import RichTextField
# Create your models here.
class answer(models.Model):
    useraname = models.CharField(max_length=50)
    userbname = models.CharField(max_length=50)
    question=models.ForeignKey(ques,on_delete=models.CASCADE)
    content=RichTextField(null=True, blank=True)
    #like=models.CharField(max_length=10)
