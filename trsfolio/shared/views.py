from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):    
    return render(request, 'shared/home.html')

def links(request):
    links = Link.objects.all()
    return render(request, 'shared/links.html', {'links': links})

def terms(request):
    return render(request, 'shared/terms.html')

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
                    from_email = 'Contact Form hugotrs.com <spam@hugotrs.com>',
                    recipient_list = ['hi@hugotrs.com'],
                )
                return HttpResponse("thanks for your message, he will be in touch as soon as possible")
            except BadHeaderError:
                return HttpResponse("Something went wrong, please refresh the site and try again :(")

    return HttpResponse("you did something wrong")