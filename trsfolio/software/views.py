from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    print (projects)
    return render(request, 'software/portfolio.html', {'projects': projects})