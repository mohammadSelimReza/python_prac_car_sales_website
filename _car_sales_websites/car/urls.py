from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name='homePage'),
    path('brand/<slug:brand_slug>/', views.product_view, name='brand_filter'),
]
