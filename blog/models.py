from datetime import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)


# Create your models here.
