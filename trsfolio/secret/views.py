from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *

# Create your views here.
def secret_letter(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        secret = get_object_or_404(SecreteLetter, code=code)
        return render(request, 'secret/secret_letter.html', {'secret': secret})
        try:
            secret = get_object_or_404(SecreteLetter, code=code)
            return render(request, 'secret/secret_letter.html', {'secret': secret})
        except:
            return render(request, 'secret/open_secret.html', {'message': 'Sorry, you are not meant to see this'})
    return render(request, 'secret/open_secret.html')
