from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cartDetailView, name = 'cart_detail'),
    path('add/<int:product_id>/', views.productAddView, name = 'product_add'),
    path('remove/<int:product_id>/', views.productRemoveView, name = 'product_remove'),
]