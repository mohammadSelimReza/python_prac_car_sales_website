from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def user_form(request):
    return render(request,'user_form.html')

def user_register(request):
    if request.method == 'POST':
        register_form = forms.register_form(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('basePage')
        
    else:
        register_form = forms.register_form()
    return render(request,'user_form.html',{'form':register_form})