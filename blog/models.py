from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile')

    def __str__(self):
        return f"{self.user.username} Profile"


class About(models.Model):
    first_name = models.CharField(max_length=212)
    last_name = models.CharField(max_length=212)
    about = models.TextField()
    image = models.ImageField(upload_to='about')
    profession = models.CharField(max_length=212)
    cv = models.FileField(upload_to='cv', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
