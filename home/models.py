from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message_box = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.email
    