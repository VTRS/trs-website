from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shared'
urlpatterns = [
    path('', views.home, name='home'),
    path('links', views.links, name='links'),
    path('terms', views.terms, name='terms'),
    path('contact', views.contact, name='contact'),
    path('hushush', views.hushush, name='hushush'),
    path('under_construction', views.under_construction, name='under_construction'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)