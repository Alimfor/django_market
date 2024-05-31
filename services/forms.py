from django import forms
from .models import Service


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title", "description", "image"]
