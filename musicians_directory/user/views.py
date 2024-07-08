from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.
def loginHere(request):
    if not request.user.is_authenticated:
        if  request.method == 'POST':
            forms = RegisterForm(request.POST)
            if forms.is_valid():
                messages.success(request, "Account Created Successfully.")
                forms.save()
        else:
            forms = RegisterForm()
        return render(request,'registration.html',{'form':forms})
    else:
        return redirect('homapage')

class userLogin(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homapage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Invalid candidate')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
# class userLogout(LogoutView):
#     def get_success_url(self):
#         return reverse_lazy('homapage')  
    
    

def joinNow(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful.")
                    return redirect('homapage')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('homapage')
        
def userLogout(request):
    logout(request)
    return redirect('homapage')