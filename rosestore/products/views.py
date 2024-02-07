from django.shortcuts import render, HttpResponse
from .models import Flower, Product

# APIs
def home(request):
    return HttpResponse(Flower.objects.all())

def products(request):
    return HttpResponse(Product.objects.all())