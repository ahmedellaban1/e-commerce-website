from django.shortcuts import render
from .models import Product, Category, ProductImage, Review
# Create your views here.


def home_page(request, *args, **kwargs):
    product = Product.objects.order_by('created_at')[:6]
    context = {
        'products': product,
        'page_title': 'Aviato | home',
    }
    return render(request, 'home-page.html', context)


def shop_page(request, *args, **kwargs):
    return render(request, 'shop.html', context={})
