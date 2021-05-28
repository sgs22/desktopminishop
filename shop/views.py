from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .models import Product, About

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://localhost:8000'

def shop_view(request, *args, **kwargs):
    product = Product.objects.first()
    return render(request, "index.html", {"product": product})

def product_overview(request, *args, **kwargs):
    product = Product.objects.first()
    return render(request, "desktopmini.html", {'product' : product})

def about_view(request, *args, **kwargs):
    queryset = About.objects.all()
    return render(request, "about.html", {"about": queryset})

def support_view(request, *args, **kwargs):
    return render(request, "support.html")

class SuccessView(TemplateView):
    template_name = "success.html"

def success_view(request):
    # context = {
    #     'session_id' : stripe.checkout.Session.retrieve(request.args.get('session_id')),
    #     'customer' : stripe.Customer.retrieve(session_id.customer)
    # }
    return render(request, "success.html")

class CancelView(TemplateView):
    template_name = "cancel.html"

#stripe.api_key = 'sk_test_51Ir0syGCqOfTY5QUzBzfXtk3SQhJlHyPQbjjNxsufbJLEIhXLX3uajsbh6cyS9mNPgz7Sdwvnhk7JE1yHH9wp1zc006Ll2M2AV'

@csrf_exempt
def checkout_view(request):
    product = Product.objects.first()
    checkout_session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    shipping_rates=['shr_1IvOERGCqOfTY5QUfjaaXvRf'],
    billing_address_collection='auto',
    shipping_address_collection={
        'allowed_countries': ['GB'],
    },  
    line_items=[
        {
            'price_data': {
                'currency': 'gbp',
                'unit_amount': int(product.price*100),
                'product': 'prod_JXUZMeZuTsN2YR', 
            },
            'adjustable_quantity': {
            'enabled': True,
            'minimum': 1,
            'maximum': 10,
            },
            'quantity': 1,
        },
    ],
    mode='payment',
    success_url=request.build_absolute_uri(reverse('success')) + '?checkout_session_id={CHECKOUT_SESSION_ID}',
    cancel_url=request.build_absolute_uri(reverse('index')),
)
    return JsonResponse({
        'checkout_session_id' : checkout_session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY,
    })

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = "sk_test_51Ir0syGCqOfTY5QUzBzfXtk3SQhJlHyPQbjjNxsufbJLEIhXLX3uajsbh6cyS9mNPgz7Sdwvnhk7JE1yHH9wp1zc006Ll2M2AV"




@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
