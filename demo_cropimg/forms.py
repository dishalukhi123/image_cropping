from django import forms
from .models import Images

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ()
