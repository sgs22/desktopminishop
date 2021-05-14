from django.contrib import admin

from .models import ProductDetail, ProductGallery, About

class ImagesInline(admin.TabularInline):
  model = ProductGallery

class ProductAdmin(admin.ModelAdmin):
  inlines = [
    ImagesInline,
  ]

admin.site.register(ProductDetail, ProductAdmin)
admin.site.register(About)