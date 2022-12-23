from django import forms
from .models import Display



class CreateDisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = '__all__'
        help_texts = {
            'location_type': 'Residential, Commercial, Non-Profit, etc.',
            'style': 'Static, Pixel, Hybrid, etc.',
            'hide_address': 'Do not display address on listings page',
            'viewer_instructions': 'Do not block driveways, listen to music on 93.7FM, etc.'
        }
