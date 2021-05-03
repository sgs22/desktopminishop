from django.db import models

class ProductDetail(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #image = models.ImageField(upload_to='products/%Y/%m/%d/', max_length=255, null=True, blank=True) 
    description = models.TextField(max_length=300, blank=True)
    release_year = models.CharField(max_length=120, blank=True)
    dimensions = models.CharField(max_length=120, blank=True)
    model_number = models.CharField(max_length=120, blank=True)
    manufacturer = models.CharField(max_length=120, blank=True)
    colour = models.CharField(max_length=120, blank=True)
    connectivity = models.CharField(max_length=120, blank=True)
    features = models.CharField(max_length=120, blank=True)
    storage_type = models.CharField(max_length=120, blank=True)
    form_factor = models.CharField(max_length=120, blank=True)
    memory_type = models.CharField(max_length=120, blank=True)
    processor = models.CharField(max_length=120, blank=True)
    gpu = models.CharField(max_length=120, blank=True)
    brand = models.CharField(max_length=120, blank=True)
    graphics_interface = models.CharField(max_length=120, blank=True)
    graphics_type = models.CharField(max_length=120, blank=True)
    operating_system = models.CharField(max_length=120, blank=True)
    tdp = models.CharField(max_length=120, blank=True)
    weight = models.CharField(max_length=120, blank=True)
    updated = models.DateTimeField(auto_now=True) 
    timestamp = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['name'] 
        verbose_name = "Product Detail"
        verbose_name_plural = "Product Details"

    def __str__(self):
        return self.name

