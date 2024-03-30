from django.shortcuts import render
from .models import *

import math
# Create your views here.
def gallery(request):
    series = Series.objects.all()
    return render(request, 'photography/gallery.html', {'series': series})

def series(request, series_id):
    series = Series.objects.get(id=series_id)
    images = series.album.images.all()
    column_length = math.ceil(images.count()/4)
    photos = []
    count = 0
    for i in range(0,4):
        if column_length <= images.count():
            column = images[:column_length]
            images = images[column_length:]
        else:
            column = images
        photos.append(column)

    return render(request, 'photography/series.html', {
        'series': series,
        'photos': photos,

    })