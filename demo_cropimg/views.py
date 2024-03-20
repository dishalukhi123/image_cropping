from django.shortcuts import render
from django.views import View
from .forms import ImageUploadForm
from django.http import JsonResponse
from .models import Images
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import os
from django.conf import settings
from django.core.files.storage import default_storage


@method_decorator(csrf_exempt, name='dispatch')
class upload_and_crop(View):
        def get(self, request):
            image_form = ImageUploadForm()
            images = Images.objects.all()
            return render(request, 'upload_image.html', {'image_form': image_form, 'images': images})
        
        def post(self, request):
            if request.method == 'POST':
                form = ImageUploadForm(request.POST, request.FILES)
                if form.is_valid():
                    try:
                        image_instance = form.save()  # Save the form but don't commit to database yet

                        # Save the instance to the database here
                        # image_instance.save()

                        # Ensure the instance has been assigned a primary key
                        if image_instance.pk is None:
                            raise ValueError("Primary key (ID) not assigned to image instance")

                        # Create a directory using the primary key as the directory name
                        upload_dir = os.path.join(settings.MEDIA_ROOT, 'upload_pic', str(image_instance.pk))
                        os.makedirs(upload_dir, exist_ok=True)

                        # Save each uploaded image to the corresponding directory
                        for field_name, file_obj in request.FILES.items():
                            image_field_path = os.path.join(upload_dir, file_obj.name)
                            with open(image_field_path, 'wb+') as destination:
                                for chunk in file_obj.chunks():
                                    destination.write(chunk)
                            setattr(image_instance, field_name, os.path.relpath(image_field_path, settings.MEDIA_ROOT))

                        # Update and save the instance with updated image fields
                        image_instance.save()

                        print("Image instance after saving:", image_instance.pk)  # Now it should print the ID
                        return JsonResponse({'message': 'Images uploaded successfully'})
                    except Exception as e:
                        return JsonResponse({'message': str(e)}, status=500)
                else:
                    return JsonResponse({'message': 'Form is not valid'}, status=400)



            

        def put(self, request, pk):
            try:
                image_instance = Images.objects.get(pk=pk)
            except Images.DoesNotExist:
                return JsonResponse({'message': 'Image not found'}, status=404)
            
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                image_form = ImageUploadForm(data, instance=image_instance)
            else:
                image_form = ImageUploadForm(request.POST, request.FILES, instance=image_instance)
            
            if request.method == 'PUT':
                if image_form.is_valid():
                    image_form.save()
                    return JsonResponse({'message': 'Image updated successfully'})
                else:
                    return JsonResponse({'errors': image_form.errors}, status=400)