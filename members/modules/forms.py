from django import forms
from members.models import Member

class Member_form(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    role_choices = [('admin', 'Administrador'), ('technician', 'Técnico'), ('operator', 'Operador')]
    role = forms.ChoiceField(choices=role_choices, required=True)
    
    class Meta:
        model = Member
        fields = ['name', 'password', 'role']