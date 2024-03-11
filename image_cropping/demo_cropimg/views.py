
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def crop_image(request):
    if request.method == 'POST':
        # Assuming you have a form with an image field
        uploaded_image = request.FILES['image']
        
        # Open the uploaded image using Pillow
        image = Image.open(uploaded_image)
        
        # Define the cropping coordinates (left, upper, right, lower)
        # You may get these coordinates from the user or calculate them programmatically
        left = 100
        upper = 100
        right = 300
        lower = 300
        
        # Crop the image
        cropped_image = image.crop((left, upper, right, lower))
        
        # Save the cropped image
        cropped_image.save('path/to/save/cropped_image.jpg')
        
        # Optionally, you can serve the cropped image as a response
        # return HttpResponse('Cropped image saved successfully')
        
    return render(request, 'crop_image.html')
