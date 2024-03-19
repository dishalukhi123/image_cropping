from django.shortcuts import render
from django.views import View
from .forms import ImageUploadForm
from django.http import JsonResponse
from .models import Images
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


@method_decorator(csrf_exempt, name='dispatch')
class upload_and_crop(View):
    def get(self, request):
        image_form = ImageUploadForm()
        images = Images.objects.all()
        return render(request, 'upload_image.html', {'image_form': image_form, 'images': images})

    def post(self, request):
        image_form = ImageUploadForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_upload = image_form.save(commit=False)
            image_upload.square = request.FILES.get('square')
            image_upload.rectangle = request.FILES.get('rectangle')
            image_upload.save()
            return JsonResponse({'message': 'Image uploaded successfully'})
        else:
            return JsonResponse({'message': 'Form is not valid'}, status=400)
        

    def put(self, request, pk):
        try:
            image_instance = Images.objects.get(pk=pk)
        except Images.DoesNotExist:
            return JsonResponse({'message': 'Image not found'}, status=404)
        
        if request.content_type == 'application/json':
            # If the data is sent as JSON
            data = json.loads(request.body)
            image_form = ImageUploadForm(data, instance=image_instance)
        else:
            # If the data is sent as form data
            image_form = ImageUploadForm(request.POST, request.FILES, instance=image_instance)
        
        if request.method == 'PUT':
            if image_form.is_valid():
                image_form.save()
                return JsonResponse({'message': 'Image updated successfully'})
            else:
                # Return form errors as JSON response
                return JsonResponse({'errors': image_form.errors}, status=400)