from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class user_register(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        
class user_update(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']