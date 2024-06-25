from django.shortcuts import render
from .models import Market, Delivery, Order, Client, Product, OrderItem
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
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
    
def process_login(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = None

        if user_type == 'client':
            try:
                user = Client.objects.get(client_email=email)
            except Client.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
                return render(request, "market/signin.html")
            
        elif user_type == 'delivery':
            try:
                user = Delivery.objects.get(delivery_email=email)
            except Delivery.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
                return render(request, "market/signin.html")

        elif user_type == 'shop':
            try:
                user = Market.objects.get(email=email)
            except Market.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
                return render(request, "market/signin.html")

        if user and user.password == password:
            request.session['user_id'] = user.id 
            request.session['user_type'] = user_type
            return redirect('home')  
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, "market/signin.html")

    return render(request, "market/signin.html")

def home(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')
    if not user_id or not user_type:
        return redirect('login')

    if user_type == 'client':
        user = Client.objects.get(id=user_id)
    elif user_type == 'delivery':
        user = Delivery.objects.get(id=user_id)
    elif user_type == 'shop':
        user = Market.objects.get(id=user_id)

    return render(request, "market/home.html", {
        'user': user,
        'user_type': user_type,
    })

def logout(request):
    if request.session.get('user_id'):
        request.session.flush()
        messages.success(request, 'You have been successfully logged out.')
    return redirect('login')