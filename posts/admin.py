from django.contrib import admin
from .models import Post, Status
from django.contrib.auth.models import Group
admin.site.register(Post)

admin.site.register(Status)

admin.site.unregister(Group)