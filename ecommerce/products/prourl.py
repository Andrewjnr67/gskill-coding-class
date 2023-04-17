from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name= 'cart'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('singleproducts/', views.singleproducts, name= 'singleproducts'),
    path('shop/', views.shop, name= 'shop'),
]