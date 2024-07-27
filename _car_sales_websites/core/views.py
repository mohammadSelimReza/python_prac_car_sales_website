from typing import Any
from django.shortcuts import render, get_object_or_404,redirect
from product.models import Brand,Car
from django.views.generic import DetailView
from product import models
from user.forms import user_comment
from django.views import View
from product.models import Purchase
from django.contrib import messages
# Create your views here.
def homePage(request,brand_slug = None):
    if brand_slug:
        brand = get_object_or_404(Brand,slug = brand_slug)
        cars = Car.objects.filter(brand_name = brand)
    else:
        cars = Car.objects.all()
         
    brand = Brand.objects.all()
    return render(request,'index.html',{'products':cars,'brands':brand, 'brand_slug': brand_slug})


class CarDetails(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'carDetails.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = user_comment(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request,*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()  # Get all comments related to the car
        comment_form = user_comment()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    
class BuyCar(View):
    def post(self,request,car_id):
        car = Car.objects.get(id=car_id)
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            messages.success(request, "Car Purchased Done")
            Purchase.objects.create(user=request.user,car=car)
        
        return redirect('homePage')