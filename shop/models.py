from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=300, blank=True)
    featured_img = models.ImageField(upload_to='products/images/', blank=True)
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
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.featured_img.url
        except:
            url = ''
        print('URL:', url)
        return url

class ProductGallery(models.Model):
    image = models.ImageField(u'images', upload_to='products/images/', blank=True)
    products = models.ForeignKey('Product', blank=True, null=True, on_delete=models.CASCADE)

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL:', url)
        return url

class About(models.Model):
    card_main_title = models.CharField(max_length=120, blank=False) 
    card_main_content = models.TextField(max_length=500, blank=True)
    card_left_title = models.CharField(max_length=120, blank=False) 
    card_left_content = models.TextField(max_length=500, blank=True)
    card_right_title = models.CharField(max_length=120, blank=False) 
    card_right_content = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "About Panel"

    def __str__(self):
        return self.card_main_title
