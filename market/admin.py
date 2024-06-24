from django.contrib import admin
from .models import Product, Order, Market, Delivery, Client

# Register your models here
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Market)
admin.site.register(Delivery)
admin.site.register(Client)
