from django.shortcuts import HttpResponse, render
from .models import (
    Flower, 
    Product,
    Basket,
    Entourage,
    Package,
    Houseplant
)
from info.models import Branch
from orders.models import Order
from gifts.models import Gift


def home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/home.html", context)

def flower_api_view(request):
    return HttpResponse(Flower.objects.all())

def product_api_view(request):
    return HttpResponse(Product.objects.all())

def basket_api_view(request):
    return HttpResponse(Basket.objects.all())

def entourage_api_view(request):
    return HttpResponse(Entourage.objects.all())

def branch_api_view(request):
    return HttpResponse(Branch.objects.all())

def package_api_view(request):
    return HttpResponse(Package.objects.all())

def houseplant_api_view(request):
    return HttpResponse(Houseplant.objects.all())

def order_api_view(request):
    return HttpResponse(Order.objects.all())

def gift_api_view(request):
    return HttpResponse(Gift.objects.all())