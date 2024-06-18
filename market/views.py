from django.shortcuts import render
from .models import Market, Delivery, Order, Client, Product, OrderItem
from django.http import HttpResponseRedirect 
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "market/index.html")

def login(request):
    pass
def register_shop(request):
    return render(request, "market/register_shop.html")

def create_shop(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        Tax_id = request.POST.get('Tax_id')
        Market.objects.create(name=name,location=address,password=password,phone=phone,email=email,Tax_id = Tax_id)
        return render(request, "market/index.html")
    else:
        return render(request, "market/register_shop.html")



