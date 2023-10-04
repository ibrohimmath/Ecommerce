from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect, HttpResponseNotFound 
from django.shortcuts import render, redirect, get_object_or_404 

from .models import Category, Product

from cart.cart import Cart
from cart.forms import CartForm


def productListView(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    # print(categories)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category) 
    return render(request, 'shop/list.html', {
        'categories': categories, 
        'products': products, 
        'category': category,
    })

def productDetailView(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug)
    form = CartForm()
    return render(request, 'shop/detail.html', {
        'product': product,
        'form': form,
    }) 
