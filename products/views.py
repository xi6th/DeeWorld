from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

class HomeView(ListView):
    model = Item
    template_name = "home.html"


def Products(request):
    return render(request,"product.html")

def checkout(request):
    return render(request,"checkout.html")

