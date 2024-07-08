from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.loginHere,name='createUser'),
    path('login/',views.userLogin.as_view(),name='joinuser'),
    path('logout/',views.LogoutView.as_view(),name='userOut'),
]
