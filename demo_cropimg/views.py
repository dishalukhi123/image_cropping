# views.py

from django.shortcuts import redirect, render
from .forms import ImageUploadForm
from .models import ImageUpload

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    last_uploaded_image = ImageUpload.objects.last()
    return render(request, 'upload_success.html', {'image': last_uploaded_image})
