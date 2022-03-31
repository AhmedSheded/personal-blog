from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.FileField(null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    comments = models.IntegerField(null=True)

    class Meta:
        ordering = ['-created_dt']

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
