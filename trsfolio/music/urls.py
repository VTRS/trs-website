from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'music'
urlpatterns = [
    path('', views.discography, name='discography'),
    path('events', views.events, name='events')
]