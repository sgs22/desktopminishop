from django.shortcuts import render

from .models import ProductDetail

def shop_view(request, *args, **kwargs):
    queryset = ProductDetail.objects.all()
    return render(request, "index.html", {"product": queryset})

def about_view(request, *args, **kwargs):
    return render(request, "about.html")