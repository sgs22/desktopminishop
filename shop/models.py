from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    featured_img = models.ImageField(upload_to='products/images/', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    finish = models.CharField(max_length=255, blank=True)
    processor = models.CharField(max_length=255, blank=True)
    memory = models.CharField(max_length=255, blank=True)
    storage = models.CharField(max_length=255, blank=True)
    video_support = models.TextField(blank=True)
    audio = models.TextField(blank=True)
    connections = models.TextField(blank=True)
    communications = models.TextField(blank=True)
    height = models.CharField(max_length=255, blank=True)
    width = models.CharField(max_length=255, blank=True)
    depth = models.CharField(max_length=255, blank=True)
    weight = models.CharField(max_length=255, blank=True)
    warranty = models.TextField(blank=True)
    in_the_box = models.TextField(blank=True)
    operating_system = models.TextField(blank=True)
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

class SupportTickets(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

