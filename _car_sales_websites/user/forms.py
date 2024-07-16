from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class user_form(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        
class profile_update(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']