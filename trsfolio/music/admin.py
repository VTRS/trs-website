from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import *


@admin.register(Ep)
class EpAdmin(admin.ModelAdmin):
    list_display = ('name', 'songs_link')

    def songs_link(self, obj):
        count = obj.songs.count()
        url = (
            reverse("admin:music_song_changelist") 
            + "?"
            + urlencode({"eps__id": f'{obj.id}'})
        )
        return format_html('<a href="{}">{} Songs</a>', url, count)
    songs_link.short_description = "Songs"

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass

