from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import URLValidator

from shared.models import Album

# Create your modeclass
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github = models.CharField(max_length=500, validators=[URLValidator()])
    link = models.CharField(max_length=500, validators=[URLValidator()])
    tags = TaggableManager()

    def __str__(self):
        return self.name

class Collaborators(models.Model):
    name = models.CharField(max_length=50)
    roles = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project_Details(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    release_date = models.CharField(max_length=8)
    status = models.CharField(max_length=50)
    screenshots = models.ForeignKey(Album, on_delete=models.CASCADE)
    technical_description = models.TextField()
    contributions = models.TextField()
    collaborators = models.ManyToManyField(Collaborators)

    def __str__(self):
        return self.project
    