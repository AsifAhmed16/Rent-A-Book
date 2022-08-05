import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Rent


def home(request):
    context = dict()
    if not request.user.is_authenticated:
        return redirect("/login")
    context['all_books'] = Book.objects.all()
    return render(request, 'management/home.html', context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Registration is Successful. Please login to continue.')
        return redirect("/login")
    else:
        form = UserCreationForm()
    return render(request, 'management/register.html', {"form": form})


@login_required()
def book_details(request, id=None):
    context = dict()
    item = Book.objects.get(id=id)
    context['item'] = item
    return render(request, 'management/details.html', context)


@login_required()
def rent_book(request, id=None):
    context = dict()
    Rent.objects.create(user_id=request.user.id,
                        book_id=Book.objects.get(id=id),
                        expired_on=datetime.datetime.now() + datetime.timedelta(days=7))
    # here the celery beat cam be used to call a schedule task after 7 days to give user the expiration of book
    messages.success(request, 'Book Successfully Rented')
    context['all_books'] = Book.objects.all()
    return render(request, 'management/home.html', context)


@login_required()
def rent_list(request):
    context = dict()
    context['items'] = Rent.objects.filter(user_id=request.user.id)
    return render(request, 'management/rent_list.html', context)
