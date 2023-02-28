from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="posts_video")

    def __str__(self):
        return str(self.videofile)

class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body = models.TextField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default = 2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args = [self.id])

