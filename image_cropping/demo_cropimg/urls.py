# urls.py
from django.urls import path
from .views import crop_image

urlpatterns = [
    path('crop/', crop_image, name='crop_image'),
]
