from django.shortcuts import render, HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request, "products/index-template.html", {
        'all_products':all_products
    })

def create_product(request):
    create_form = ProductForm()
    return render(request, 'products/create-template.html', {
        'form':create_form
    })