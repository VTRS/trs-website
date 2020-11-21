from django.shortcuts import render
from .models import *

# Create your views here.
def gallery(request):
    series = Series.objects.all()
    return render(request, 'photography/gallery.html', {'series': series})