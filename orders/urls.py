from django.urls import path, include 

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.orderCreateView, name = 'order_create'),
] 