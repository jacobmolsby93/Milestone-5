from django import forms
from .models import ServiceRequestModel, Services


class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestModel
        fields = ('full_name', 'email', 'phone_number', 'ideas')
        

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Services.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
