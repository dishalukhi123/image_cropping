# urls.py
from django.urls import path
from .views import crop_image
from . import views


urlpatterns = [
    path('crop/', crop_image, name='crop_image'),
     path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
