from django import forms
from carbook_app import models

class carbooking_data(forms.ModelForm):
    class Meta:
        model = models.carbooking
        fields = '__all__'