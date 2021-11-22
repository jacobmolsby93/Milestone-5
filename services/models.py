from django.db import models

# Create your models here.


class Services(models.Model):
    """
    A model for the services that the page is providing
    """
    class Meta:
        verbose_name_plural = 'Services'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pricing_description = models.TextField(max_length=254)
    service_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Testamonials(models.Model):
    """
    A model for the testamonials
    """
    class Meta:
        verbose_name_plural = 'Testamonials'
        
    testamonial_image = models.ImageField(null=True, blank=True)
    testamonial_review = models.TextField()
    persons_name = models.CharField(max_length=50)
    persons_work = models.CharField(max_length=50)
    testamonial_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    
    def __str__(self):
        return self.persons_name

