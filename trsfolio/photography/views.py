from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def gallery(request):
    collection = Series.objects.all()
    return render(request, 'photography/gallery.html', {'collection': collection})

def series(request, id):
    series = get_objecto_or_404(Series, id=id)
    return render(request, 'photography/series.html', {'series':series})