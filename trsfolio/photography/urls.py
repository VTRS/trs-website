from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photography'
urlpatterns = [
    path('', views.gallery, name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)