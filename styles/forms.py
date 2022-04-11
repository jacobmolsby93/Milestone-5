from django import forms
from .models import ShopStyles


class StyleForm(forms.ModelForm):

    class Meta:
        model = ShopStyles
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'style_image': 'Image',
            'sku': 'SKU',
            'style_name': 'Style Name',
            'style_price': 'Price',
            'style_description': 'Description',
            'url_field': 'URL'
        }

        for field in self.fields:            
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

