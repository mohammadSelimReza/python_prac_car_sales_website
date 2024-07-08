from django.urls import path
from . import views

urlpatterns = [
    path('addAlbum/',views.create_album.as_view(),name='newAlbum'),
    path('update/',views.update_album.as_view(),name='updateAlbum'),
]
