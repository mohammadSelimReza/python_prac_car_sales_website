from django.shortcuts import render
from .models import Car
# Create your views here.
def product_view(request):
    data = Car.objects.all()
    return render(request,'products.html',{'data':data})