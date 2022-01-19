from django.urls import path
from .views import (
    checkout,
    HomeView,
    Products

)
app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home', HomeView.as_view(), name='home'),
    path('checkout/', checkout),
    path('product/', Products, name='product'),
]
