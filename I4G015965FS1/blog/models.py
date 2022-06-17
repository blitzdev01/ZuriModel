from turtle import title
from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()