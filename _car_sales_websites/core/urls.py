from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage,name='homePage'),
    path('brand/<slug:brand_slug>/',views.homePage,name='brand_filter'),
    path('details/<int:id>',views.CarDetails.as_view(),name='carDetails'),
]
