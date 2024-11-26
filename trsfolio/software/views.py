from django.shortcuts import render, get_object_or_404
from .models import *

import math

# Create your views here.
def portfolio(request):
    projects = Project.objects.all().order_by('-id')
    print (projects)
    return render(request, 'software/portfolio.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    images = project.projectdetails.screenshots.images.all()
    
    column_length = math.ceil(images.count()/2)
    screenshots = []
    count = 0
    for i in range(0,2):
        if column_length <= images.count():
            column = images[:column_length]
            images = images[column_length:]
        else:
            column = images
        screenshots.append(column)
        

    return render(request, 'software/project_detail.html', {'project':project, 'screenshots':screenshots})