from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'phone_number',
                  'subject', 'message_box',)
    

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
            'subject': 'Subject',
            'message_box': 'Message'
        }
        
        for field in self.fields:
            if field != 'message_box':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder