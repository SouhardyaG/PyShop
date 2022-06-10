from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /product -> index
# uniform resiurce locator
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse("New Products")
