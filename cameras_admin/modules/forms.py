from django import forms
from cameras_admin.models import Camera

class CreateCamera_form(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    rtsp = forms.CharField(required=True)
    peop_c_service = forms.BooleanField(required=False)
    face_rec_service = forms.BooleanField(required=False)
    vehicules_service = forms.BooleanField(required=False)
    class Meta:
        model = Camera
        fields = ['name', 'rtsp', 'peop_c_service', 'face_rec_service', 'vehicules_service']
    
