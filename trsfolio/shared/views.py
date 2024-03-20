from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from shared.models import File

# Create your views here.
def home(request): 
    presskit =  File.objects.get(name='presskit') 
    return render(request, 'shared/home.html', {'presskit': presskit})

def links(request):
    links = Link.objects.all()
    return render(request, 'shared/links.html', {'links': links})

def terms(request):
    return render(request, 'shared/terms.html')

def under_construction(request):
    return render(request, 'shared/under_construction.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        if name and message and contact:
            try:
                send_mail(
                    subject = name + ' is trying to reach you',
                    message = 'Name: ' + name + '<br>Contact' + contact + '<br>Messsage: ' + message,
                    from_email = 'Contact Form victrs.art <contact@victrs.art>',
                    recipient_list = ['vic@victrs.art'],
                )
                return HttpResponse("thanks for your message, he will be in touch as soon as possible")
            except BadHeaderError:
                return HttpResponse("Something went wrong, please refresh the site and try again :(")

    return HttpResponse("you did something wrong")