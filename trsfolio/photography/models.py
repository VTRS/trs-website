from django.db import models

# Create your modeclass
class Series(models.Model):
    title = models.CharField(max_length=100)
    argument = models.TextField()

    def __str__(self):
        return self.title