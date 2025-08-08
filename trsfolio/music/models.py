from django.db import models

class Ep(models.Model):
    name = models.CharField(max_length=255)
    artwork = models.ImageField(upload_to='artwork', blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    apple = models.URLField(blank=True, null=True)
    soundcloud = models.URLField(blank=True, null=True)
    bandcamp = models.URLField(blank=True, null=True)
    presave = models.URLField(blank=True, null=True)
    amazon = models.URLField(blank=True, null=True)
    tidal = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    artists = models.ManyToManyField('Artist', related_name='songs', blank=True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    maps = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    instagram = models.URLField(blank=True, null=True)
    soundcloud = models.URLField(blank=True, null=True)
    apple_music = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    bandcamp = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    artists = models.ManyToManyField(Artist, related_name='events', blank=True)
    date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey(Venue, related_name='events', on_delete=models.CASCADE)
    flyer = models.ImageField(upload_to='flyer', blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name + '-' + str(self.date)

# class Lineup(models.Model):
#     artist = models.ForeignKey(Artist, related_name='lineups', on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, related_name='lineups', on_delete=models.CASCADE)


#     def __str__(self):
#         return self.artist.name - self.event.name


    






