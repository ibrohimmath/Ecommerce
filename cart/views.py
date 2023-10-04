from django.http import Http404, HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_POST
from django.urls import reverse

from .cart import Cart
from .forms import CartForm

from shop.models import Category, Product

def cartDetailView(request):
    cart = Cart(request)
    for item in cart:  
        item['form'] = CartForm(initial = {
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'cart/detail.html', {
        'cart': cart,
    })

@require_POST
def productAddView(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, cd['quantity'], cd['override'])
    return redirect(reverse('cart:cart_detail'))

@require_POST
def productRemoveView(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.remove(product)    
    return redirect(reverse('cart:cart_detail'))
