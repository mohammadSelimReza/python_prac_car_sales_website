from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile
from .forms import SignUpForm, ChangePasswordForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully. You can now login.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authentication/login.html')

@login_required
def profile(request):
    return render(request, 'authentication/profile.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to maintain the user's session
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'authentication/change_password.html', {'form': form})
