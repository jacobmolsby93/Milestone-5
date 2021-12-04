from django.db import models

# Create your models here.


class ShopStyles(models.Model):
    """
    A model for the shopnow styles
    """
    class Meta:
        verbose_name_plural = 'Shop Styles'
        
    style_image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    style_name = models.CharField(max_length=254)
    style_price = models.DecimalField(max_digits=6, decimal_places=2)
    style_description = models.TextField()
    url_field = models.URLField(null=True, blank=False, default='')

    def __str__(self):
        return self.style_name
