from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView
from .models import *
from django.contrib import messages

# Create your views here.

class HomeView(ListView):
    model = Item
    paginate_by = 1
    template_name = 'home.html'

class ItemDetailsView(DetailView):
    model = Item
    template_name = 'product.html'

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item, 
        user = request.user, 
        ordered = False
    )
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        order = Order.objects.create(user=request.user)
        order.item.add(order_item)
    return redirect("core:product", kwargs={
        'slug': slug
    })

class OrderSummaryView(DetailView):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user = self.request.user, ordered =False)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order')
            return redirect('/')

        return render(self.request, 'order-summary.html')

def checkout(request):
    context = {}
    return render(request,"checkout.html",context)
