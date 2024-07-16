from django.shortcuts import render, get_object_or_404
from product.models import Brand,Car
# Create your views here.
def homePage(request,brand_slug = None):
    if brand_slug:
        brand = get_object_or_404(Brand,slug = brand_slug)
        cars = Car.objects.filter(brand_name = brand)
    else:
        cars = Car.objects.all()
         
    brand = Brand.objects.all()
    return render(request,'index.html',{'products':cars,'brands':brand, 'brand_slug': brand_slug})