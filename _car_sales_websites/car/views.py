from django.shortcuts import render, get_object_or_404
from .models import Car, Brand

def product_view(request, brand_slug=None):
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        data = Car.objects.filter(brand=brand)
    else:
        data = Car.objects.all()
    
    brands = Brand.objects.all()
    return render(request, 'products.html', {'data': data, 'brands': brands, 'brand_slug': brand_slug})
