from django import forms
from .models import ServiceRequestModel, Services


class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestModel
        fields = ('full_name', 'email', 'phone_number', 'ideas')
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholder and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'ideas': 'Idea',
        }
        
        for field in self.fields:            
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = (
            'name',
            'description',
            'price',
            'pricing_description',
            'service_image',
            'sku')

    def __init__(self, *args, **kwargs):
        """
        Add placeholder and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Service Name',
            'description': 'Service Description',
            'price': 'Price',
            'pricing_description': 'Price Description',
            'service_image': 'Service Image',
            'sku': 'SKU - Unique'
        }
        
        for field in self.fields:            
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

