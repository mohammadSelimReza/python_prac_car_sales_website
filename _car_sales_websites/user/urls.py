from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.createUser,name='useRegister'),
    path('login/',views.user_login,name='userLogin'),
    path('logout/',views.user_logout,name='userOut'),
    path('profile/',views.user_profile,name='usrProfile'),
    path('order/',views.user_purhcased,name='userOrder'),
    path('update/',views.user_update,name='profileUpdate'),
    path('update-password/',views.password_change,name='updatePass')
]
