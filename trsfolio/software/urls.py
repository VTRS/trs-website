from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'software'
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('project_detail/<int:project_id>', views.project_detail, name='project_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
