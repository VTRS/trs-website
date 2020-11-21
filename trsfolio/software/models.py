from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import URLValidator

# Create your modeclass
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github = models.CharField(max_length=500, validators=[URLValidator()])
    link = models.CharField(max_length=500, validators=[URLValidator()])
    tags = TaggableManager()

    def __str__(self):
        return self.name
    
