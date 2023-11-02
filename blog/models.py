import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify

from user.models import User


def post_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/posts/", filename)


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="liked_posts"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to=post_image_file_path)

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="liked_comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.user.email}"
