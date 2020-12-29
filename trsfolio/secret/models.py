from django.db import models
from shared.models import Image

# Create your modeclass
class SecreteLetter(models.Model):
    title = models.CharField(max_length=100)
    argument = models.TextField()
    artwork = models.ForeignKey(Image, on_delete=models.CASCADE)
    link_to_soundcloud = models.CharField(max_length=200)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.title