from django.urls import path, include 

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.productListView, name = 'product_list'),
    path('<slug:category_slug>/', views.productListView, name = 'product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.productDetailView, name = 'product_detail'),
]