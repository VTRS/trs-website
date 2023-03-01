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

class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    maps = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# class Artist(models.Model):
#     name = models.CharField(max_length=255)
#     instagram = models.URLField(blank=True, null=True)
#     soundcloud = models.URLField(blank=True, null=True)
#     spotify = models.URLField(blank=True, null=True)
#     apple_music = models.URLField(blank=True, null=True)
#     website = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey(Venue, related_name='events', on_delete=models.CASCADE)
    instagram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name + '-' + str(self.date)

# class Lineup(models.Model):
#     artist = models.ForeignKey(Artist, related_name='lineups', on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, related_name='lineups', on_delete=models.CASCADE)


#     def __str__(self):
#         return self.artist.name - self.event.name


    






