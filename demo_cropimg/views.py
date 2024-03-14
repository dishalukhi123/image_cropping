# views.py

from django.shortcuts import render
from .models import CroppedImage
from .forms import ImageUploadForm

def upload_and_crop(request):
    form = ImageUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        images = CroppedImage.objects.all()
        return render(request, 'upload_image.html', {'images': images})
    context = {'form': form}
    return render(request, 'upload_image.html', context)
