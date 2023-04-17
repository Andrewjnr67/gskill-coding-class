from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def shop(request):
    return render(request, 'products/shop.html')

def singleproducts(request):
    return render(request, 'products/singleproducts.html')