from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)
    Tax_id = models.CharField(max_length=10, default=None)
    password = models.CharField(max_length=255, default='default_password_value')

    def __str__(self):
        return f"{self.name}"

class Delivery(models.Model):
    delivery_name = models.CharField(max_length=64)
    delivery_phone = models.CharField(max_length=15)
    delivery_email = models.EmailField(max_length=64)
    password = models.CharField(max_length=255, default='default_password_value')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.delivery_name}"

class Client(models.Model):
    client_name = models.CharField(max_length=64)
    client_phone = models.CharField(max_length=15)
    client_email = models.EmailField(max_length=64)
    password = models.CharField(max_length=255, default='default_password_value')
    client_address = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.client_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=64)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_stocks = models.IntegerField(default=0)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_delivered = models.BooleanField(default=False)
    products = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE,default=0)
    
    def __str__(self):
        return f"Order {self.id} by {self.client.client_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} for order {self.order.id}"
