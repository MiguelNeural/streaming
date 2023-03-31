from django import forms
from cameras_admin.models import Camera

class CreateCamera_form(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['name', 'rtsp']
