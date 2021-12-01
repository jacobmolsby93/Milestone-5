from django.contrib import admin
from .models import (
    Services, ServiceRequestModel, Testamonials
)

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'service_image',
    )


class TestamonialAdmin(admin.ModelAdmin):
    list_display = (
        'persons_name',
        'persons_work',
        'testamonial_image',
        'testamonial_review',
        'testamonial_rating',
    )

class ServiceRequestModelAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'user',
        'full_name',
        'email',
        'phone_number',
    )
    

admin.site.register(Services, ServiceAdmin)
admin.site.register(Testamonials, TestamonialAdmin)
admin.site.register(ServiceRequestModel, ServiceRequestModelAdmin)