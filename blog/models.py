from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description: models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content: models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

