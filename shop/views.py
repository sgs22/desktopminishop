from django.shortcuts import render

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Product, About

stripe.api_key = settings.STRIPE_SECRET_KEY


def shop_view(request, *args, **kwargs):
    product = Product.objects.first()
    return render(request, "index.html", {"product": product})

def product_overview(request, *args, **kwargs):
    product = Product.objects.first()
    return render(request, "desktopmini.html", {"product": product})

def about_view(request, *args, **kwargs):
    queryset = About.objects.all()
    return render(request, "about.html", {"about": queryset})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")

# Stripe Checkout Views

# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         product_id = self.kwargs["pk"]
#         product = Product.objects.get(id=product_id)
#         YOUR_DOMAIN = "http://127.0.0.1:8000"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'gbp',
#                         'unit_amount': product.price,
#                         'product_data': {
#                             'name': product.name
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             metadata={
#                 "product_id": product.id
#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })

# class ProductLandingPageView(TemplateView):
#     template_name = "desktopmini.html"

#     def get_context_data(self, **kwargs):
#         product = Product.objects.get(name="DesktopMini")
#         context = super(ProductLandingPageView, self).get_context_data(**kwargs)
#         context.update({
#             "product": product,
#             "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
#         })
#         return context



class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"