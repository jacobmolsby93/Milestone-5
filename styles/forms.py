from django import forms
from .models import ShopStyles


class StyleForm(forms.ModelForm):

    class Meta:
        model = ShopStyles
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ShopStyles.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
