from django import forms
from django.forms import ModelForm

from .models import Display

# class CreateDisplayForm(forms.Form):
#     display_name = forms.CharField(label="Display Name", max_length=255)

class CreateDisplayForm(ModelForm):
    class Meta:
        model = Display
        fields = '__all__'
