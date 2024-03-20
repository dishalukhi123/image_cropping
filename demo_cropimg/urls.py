# urls.py

from django.urls import path
from . import views
from .views import upload_and_crop
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('crop-image/', upload_and_crop.as_view(), name='upload_and_crop'),
    path('crop-image/<int:pk>/', upload_and_crop.as_view(), name='update_image'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)