from django.db import models
from shared.models import Album

# Create your modeclass
class Series(models.Model):
    title = models.CharField(max_length=100)
    argument = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title