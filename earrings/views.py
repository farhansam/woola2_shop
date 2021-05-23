from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Earring, Collection
from .forms import EarringForm, SearchForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def home(request):
    return render(request, 'earrings/home-template.html')


def story(request):
    return render(request, 'earrings/story-template.html')


def collections(request):
    return render(request, 'earrings/collections-template.html')


def restricted(request):
    return render(request, 'earrings/restricted-template.html')


def allowed(user):
    return user.is_staff


@login_required
def index(request):
    earrings = Earring.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'name' in request.GET and request.GET['name']:
            name = request.GET['name']
            queries = queries & Q(name__icontains=name)

        if 'collection' in request.GET and request.GET['collection']:
            print("adding collection")
            collection = request.GET['collection']
            queries = queries & Q(collection__in=collection)

        earrings = earrings.filter(queries)

    collections = Collection.objects.all()
    search_form = SearchForm(request.GET)
    return render(request, 'earrings/index-template.html', {
        'earrings': earrings,
        'collections': collections,
        'search_form': search_form
    })


@login_required
@user_passes_test(allowed, login_url='/restricted/')
def create_earring(request):
    if request.method == 'POST':
        create_form = EarringForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"New earring {create_form.cleaned_data['name']} has been created")
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


@login_required
@user_passes_test(allowed, login_url='/restricted/')
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


@login_required
@user_passes_test(allowed, login_url='/restricted/')
def delete_earring(request, earring_id):
    earring_to_delete = get_object_or_404(Earring, pk=earring_id)
    if request.method == 'POST':
        earring_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'earrings/delete-template.html', {
            "earring": earring_to_delete
        })