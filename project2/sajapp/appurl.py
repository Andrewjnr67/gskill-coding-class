from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('content/', views.content, name= 'content'),
    path('product/', views.product, name= 'product' ),
]