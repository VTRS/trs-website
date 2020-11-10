from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'software/portfolio.html')