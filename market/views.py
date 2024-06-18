from django.shortcuts import render
# from . import util  # Comment this line if `util.py` does not exist
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
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        
