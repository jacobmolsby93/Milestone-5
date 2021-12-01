from django import forms
from .models import ServiceRequestModel


class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestModel
        fields = ('full_name', 'email', 'phone_number', 'ideas')
        