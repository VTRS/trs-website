from django.db import models

class Ep(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='audio')
    artist = models.CharField(max_length=500)
    ep = models.ForeignKey(
        Ep, 
        related_name='songs',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return self.name


