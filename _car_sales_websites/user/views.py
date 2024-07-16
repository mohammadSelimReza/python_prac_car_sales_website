from . import forms
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def createUser(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method == 'POST':
            register_form = forms.user_form(request.POST)
            if register_form.is_valid():
                messages.success(request, "Account Created Successfully.")
                register_form.save()
                return redirect('homePage')
                
        else:
            register_form = forms.user_form()
        return render(request,'user_from.html',{'form':register_form,'type':'Register Here','btn_type':'Register'})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
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
        return render(request,'user_from.html',{'form':login_form,'type':'Login Here','btn_type':'Login'})

@login_required
def user_logout(request):
    logout(request)
    return redirect('homePage')

@login_required
def user_update(request):
    if request.method == 'POST':
        update_form = forms.profile_update(request.POST,instance = request.user)
        if update_form.is_valid():
            messages.success(request, "Profile Update Successfully.")
            update_form.save()
            return redirect('homePage')
            
    else:
        update_form = forms.profile_update(instance = request.user)
    return render(request,'user_from.html',{'form':update_form,'type':'Update Your Profile','btn_type':'Update'})


@login_required
def password_change(request):
    if request.method == 'POST':
        pass_change = PasswordChangeForm(data=request.POST,user=request.user)
        if pass_change.is_valid():
            pass_change.save()
            messages.success(request, "Password Changed Successfully.")
            update_session_auth_hash(request,pass_change.user)
            logout(request)
            return redirect('userLogin')
            
    else:
        pass_change = PasswordChangeForm(user=request.user)
    return render(request,'user_from.html',{'form':pass_change,'type':'Update Password Here','btn_type':'Change Password'})

        