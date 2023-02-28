from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.urls import reverse


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="")
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=256)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )

    def __str__(self):
            return self.name + ": " + str(self.videofile)