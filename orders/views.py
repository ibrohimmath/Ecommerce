from django.http import Http404, HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse  

from .models import Order, OrderItem
from .forms import OrderForm      

from cart.cart import Cart

from .tasks import order_created

def orderCreateView(request):
    cart = Cart(request)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    product = item['product'],
                    quantity = item['quantity'],
                    price = item['price'],
                )
            # launch asynchronous task
            order_created.delay(order.id)
            cart.clear()
            return render(request, 'orders/created.html', {'order': order,})
    return render(request, 'orders/create.html', {
        'form': form,
        'cart': cart,
    })
