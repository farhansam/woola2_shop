from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Earring
from .forms import EarringForm

# Create your views here.


def index(request):
    all_earrings = Earring.objects.all()
    return render(request, "earrings/index-template.html", {
        'all_earrings': all_earrings
    })


def create_earring(request):
    if request.method == 'POST':
        create_form = EarringForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'earrings/create-template.html', {
                'form': create_form
            })
    else:
        create_form = EarringForm()
        return render(request, 'earrings/create-template.html', {
            'form': create_form
        })


def update_earring(request, earring_id):
    earring_being_updated = get_object_or_404(Earring, pk=earring_id)

    if request.method == 'POST':
        update_form = EarringForm(request.POST, instance=earring_being_updated)

        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'earrings/update-template.html', {
                'form': update_form
            })
    else:
        update_form = EarringForm(instance=earring_being_updated)
        return render(request, 'earrings/update-template.html', {
            'form': update_form
        })


def delete_earring(request, earring_id):
    earring_to_delete = get_object_or_404(Earring, pk=earring_id)
    if request.method == 'POST':
        earring_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'earrings/delete-template.html', {
            "earring": earring_to_delete
        })