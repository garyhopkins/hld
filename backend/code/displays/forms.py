from django import forms

from .models import Display



class CreateDisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = '__all__'
