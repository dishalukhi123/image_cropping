from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image
from .models import UserProfile
from .forms import ProfilePictureForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout


def crop_image(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form to the database
            form.save()
            
            # Get the uploaded image instance
            uploaded_image = form.instance.profile_picture
            
            # Open the uploaded image using Pillow
            image = Image.open(uploaded_image.path)
            
            # Define the cropping coordinates (left, upper, right, lower)
            # You may get these coordinates from the user or calculate them programmatically
            left = 100
            upper = 100
            right = 300
            lower = 300
            
            # Crop the image
            cropped_image = image.crop((left, upper, right, lower))
            
            # Save the cropped image
            cropped_image.save(uploaded_image.path)
            
            # Optionally, you can serve the cropped image as a response
            # return HttpResponse('Cropped image saved successfully')
            
            return redirect('success_url')  # Redirect to a success URL after processing
    else:
        form = ProfilePictureForm()
    return render(request, 'index.html', {'form': form})