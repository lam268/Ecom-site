from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name = 'item_list'),
    path('checkout/', checkout, name = 'checkout'),
    path('product/<slug>', ProductDetailView.as_view(), name = 'product'),
]