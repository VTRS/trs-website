from django.db import models

# Create your models here.
def get_upload_path(instance, filename):
    model = instance.album.name
    name = model.replace(' ', '_')
    return f'/images/{name}'

def get_upload_track_path(instance, filename):
    return f'files'

class Album(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    thumbnail = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_upload_track_path)

    def __str__(self):
        return self.name