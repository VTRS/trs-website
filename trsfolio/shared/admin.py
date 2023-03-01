from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'images_link')

    def images_link(self, obj):
        count = obj.images.count()
        url = (
            reverse("admin:shared_image_changelist") 
            + "?"
            + urlencode({"albums__id": f'{obj.id}'})
        )
        return format_html('<a href="{}">{} Images</a>', url, count)
    images_link.short_description = "Itudents"

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link)