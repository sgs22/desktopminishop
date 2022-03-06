from django.contrib import admin

from .models import Product, ProductGallery, About, SupportTickets

class ImagesInline(admin.TabularInline):
  model = ProductGallery

class ProductAdmin(admin.ModelAdmin):
  inlines = [
    ImagesInline,
  ]

admin.site.register(Product, ProductAdmin)
admin.site.register(About)
admin.site.register(SupportTickets)