from django.db import models
from django import forms
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
TAGS = (
    ('select','select'),
    ('django','django'),
    ('python','python'),
    ('sqlite','sqlite'),
    ('blog','blog'),
    ('text','text'),
    ('pin','pin'),
    ('blog post','blog post'),
    ('post','post'),
    ('develop','develop'),
    ('web','web'),
    ('coding','coding'),
    ('web development','web development'),
    ('natural','select'),
)
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    tags = models.CharField(max_length=255, choices=TAGS, default='select')
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_image = models.ImageField(default = 'default', upload_to='post_image')
    def __str__(self):
        return self.content
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title
#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={"pk": self.pk})
