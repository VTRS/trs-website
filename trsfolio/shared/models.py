from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    thumbnail = models.ImageField(upload_to='images', null=True, blank=True)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.name