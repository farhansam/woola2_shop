from django.shortcuts import render, HttpResponse
from .models import Earring
from .forms import EarringForm

# Create your views here.
def index(request):
    all_earrings = Earring.objects.all()
    return render(request, "earrings/index-template.html", {
        'all_earrings':all_earrings
    })

def create_earring(request):
    create_form = EarringForm()
    return render(request, 'earrings/create-template.html', {
        'form':create_form
    })