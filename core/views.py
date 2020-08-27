from django.shortcuts import render
from django.conf import settings
from django.views.generic import View, ListView, DetailView
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

class ProductDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


def checkout(request):
    context = {}
    return render(request,"checkout-page.html",context)
