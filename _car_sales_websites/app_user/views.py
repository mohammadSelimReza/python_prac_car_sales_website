from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        register_form = forms.user_register(request.POST)
        if register_form.is_valid():
            messages.success(request, "Account Created Successfully.")
            register_form.save()
            return redirect('homePage')
        
    else:
        register_form = forms.user_register()
    return render(request,'user_form.html',{'form':register_form,'type':'Register Here','btn_type':'Create New User'})
            
def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_password = login_form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_password)
            if user is not None:
                login(request,user)
                messages.success(request, "Login successful.")
                return redirect('homePage')
    else:
        login_form = AuthenticationForm()
    return render(request,'user_form.html',{'form':login_form,'type':'Login Here','btn_type':'Login'})

def user_logout(request):
    logout(request)
    return redirect('homePage')

def user_update(request):
    if request.method == 'POST':
        update_form = forms.user_update(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('homePage')
    else:
        update_form = forms.user_update(instance=request.user)
    return render(request,'user_form.html',{'form':update_form,'type':'Update Your Profile','btn_type':'Update'})