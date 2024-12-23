from django.shortcuts import render
from .models import *
from django.utils import timezone


# Create your views here.
def discography(request):
    eps = Ep.objects.all().order_by('-release_date')
    return render(request, 'music/discography.html', {'eps': eps})

def events(request):
    events = Event.objects.filter(end_date__gte=timezone.now()).order_by('date')
    past_events = Event.objects.filter(end_date__lt=timezone.now()).order_by('-date')
    return render(request, 'music/events.html', {'events': events, 'past_events': past_events})