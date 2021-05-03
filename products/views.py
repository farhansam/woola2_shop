from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request, "products/index-template.html", {
        'all_products':all_products
    })