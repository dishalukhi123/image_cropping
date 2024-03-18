from django.shortcuts import render
from .forms import ImageUploadForm
from django.http import JsonResponse
from .models import Images

def upload_and_crop(request):
      if request.method == 'POST':
        image_form = ImageUploadForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_upload = image_form.save(commit=False)
            image_upload.square = request.FILES['square']
            image_upload.rectangle = request.FILES['rectangle']
            image_upload.save()
            return JsonResponse({'message': 'Image uploaded successfully'})
        else:
            return JsonResponse({'message': 'Form is not valid'}, status=400)
      else:
        image_form = ImageUploadForm()
      images = Images.objects.all()
      return render(request, 'upload_image.html', {'image_form': image_form, 'images': images})

