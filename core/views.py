from django.shortcuts import render
from django.conf import settings
from django.views.generic import View, ListView, DetailView
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = Item
    template_name = 'product.html'


def checkout(request):
    context = {}
    return render(request,"checkout.html",context)
