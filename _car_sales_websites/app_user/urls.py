from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.create_user,name='createUser'),
    path('login/',views.user_login,name='userLogin'),
    path('logout/',views.user_logout,name='userOut'),
    path('update/',views.user_update,name='userUpdate'),
]
