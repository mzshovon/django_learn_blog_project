from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default', upload_to='profile_image')

def __str__(self):
    return f'{self.user.username} Profile'

def save(self):

    super.save()
    pic = Image.open(self.image.path)

    if pic.width > 300 or pic.height > 300:
        output_size = (300,300)
        pic.thumbnail(output_size)
        pic.save(self.image.path)

