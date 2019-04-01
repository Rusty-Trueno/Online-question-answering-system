from django.db import models
from django.contrib.auth.models import User
from answer.models import answer
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.ForeignKey(answer,on_delete=models.CASCADE)
    content =RichTextField()
    like = models.CharField(max_length=10)


