from django.shortcuts import render
from .models import Product, Category, ProductImage, Review
from django.shortcuts import get_object_or_404

# Create your views here.


def home_page(request, *args, **kwargs):
    product = Product.objects.order_by('created_at')[:6]
    context = {
        'products': product,
        'page_title': 'Aviato | home',
    }
    return render(request, 'home-page.html', context)


def product_details(request, *args, **kwargs):
    product = get_object_or_404(Product, slug=kwargs['slug'], id=kwargs['id'])
    reviews = Review.objects.filter(product_id=product)
    image = [product.image.url] + [img.image.url for img in ProductImage.objects.filter(product_id=product)]
    context = {
        'product': product,
        'reviews': reviews,
        'image': image,
        'page_title': 'Aviato | product-single',
    }
    return render(request, 'product-single.html', context)


def shop_page(request, *args, **kwargs):
    return render(request, 'shop.html', context={})
