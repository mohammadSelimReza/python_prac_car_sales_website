from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.create_musician.as_view(), name='createMusician'),
    path('edit/<int:id>/', views.update_musician.as_view(), name='update'),
    path('delete/<int:id>/', views.delete_post, name='delete'),
]
