from django.db import models
from django import forms
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description: models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})

class Post(models.Model):
    title = models.CharField(max_length=255)
    content: models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})
    

