# urls.py

from django.urls import path
from .views import upload_image, upload_success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('success/', upload_success, name='upload_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

