from django.shortcuts import render
from .models import *


# Create your views here.
def discography(request):
    tracks = Song.objects.all()

    return render(request, 'music/discography.html', {'tracks': tracks})