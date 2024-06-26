from django.shortcuts import render, HttpResponse
from home.models import Books, custumber, Sports
from home.models import Product
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        desc = request.POST.get("desc")
        contact = custumber(name=name, email=email, number=number, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent !")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def onsale(request):
    return render(request, "onsale.html")


def kitchen(request):
    return render(request, "kitchen.html")


def order(request):
    return render(request, "order.html")


def cart(request):
    return render(request, "cart.html")


def product_list(request):
    products = (
        Product.objects.all()
    )  # Adjust queryset as needed (e.g., filter by category)
    return render(request, "clothes.html", {"products": products})


def books(request):
    books = Books.objects.all()  # Adjust queryset as needed (e.g., filter by category)
    return render(request, "Books.html", {"books": books})


def sports(request):
    sports = (
        Sports.objects.all()
    )  # Adjust queryset as needed (e.g., filter by category)
    return render(request, "Sports.html", {"sports": sports})
