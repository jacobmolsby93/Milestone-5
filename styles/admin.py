from django.contrib import admin
from .models import ShopStyles
# Register your models here.


class StylesAdmin(admin.ModelAdmin):
    list_display = (
        'style_name',
        'style_image',
        'style_price',
        'sku',
        'style_description',
        'url_field'
    )

admin.site.register(ShopStyles, StylesAdmin)
    

    

