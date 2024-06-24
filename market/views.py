from django.shortcuts import render
from .models import Market, Delivery, Order, Client, Product, OrderItem
from django.http import HttpResponseRedirect 
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "market/index.html")

def login(request):
    return render(request, "market/signin.html")
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



def register_delivery(request):
    
    return render(request, "market/register_delivery.html")


def create_delivery(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        plate_number = request.POST.get('plate_number')
        Delivery.objects.create(delivery_name=name,password=password,delivery_phone=phone,delivery_email=email,plate_number = plate_number)
        return render(request, "market/signin.html")
    else:
        return render(request, "market/register_delivery.html")
    
def register_client(request):
    return render (request, "market/register_client.html")

def custom_404_page(request):
    return render(request, "market/404.html")

def create_client(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address')
        Client.objects.create(client_name=name,password=password,client_phone=phone,client_email=email, client_address = address)
        return render(request, "market/signin.html")
    else:
        return render(request, "market/register_delivery.html")