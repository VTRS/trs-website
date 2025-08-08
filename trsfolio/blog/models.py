from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='blog/thumbnails/')
    summary = models.TextField()
    content = models.TextField()
    public = models.BooleanField(default=False)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
