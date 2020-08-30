from django import forms
from .models import News


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = News
        fields = ('image',)