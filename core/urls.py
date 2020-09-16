from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name = 'item_list'),
    path('order-summary/', OrderSummaryView.as_view(), name = 'order_summary'),
    path('checkout/', checkout, name = 'checkout'),
    path('product/<slug>', ItemDetailsView.as_view(), name = 'product'),
    path('add-to-cart/<slug>', add_to_cart, name = 'add_to_cart')
]