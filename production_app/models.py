from django.db import models
from customer_app.models import City, Customer, Address

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=50)
    menu_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user_id
    def __str__(self):
        return self.menu_name

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    supplier_phone = models.CharField(max_length=15)
    supplier_email = models.EmailField(max_length=100)
    supplier_address = models.CharField(max_length=255)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='suppliers')
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.supplier_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=100)  # Renamed from 'product' for clarity
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  # Uncomment if needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=50, unique=True)  # Unique order number
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set to the current date and time when created
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')  # ForeignKey to Customer
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders')  # ForeignKey to Address

    def __str__(self):
        return f"Order #{self.order_number} by {self.customer_id.first_name} {self.customer_id.last_name}"

class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_details')
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.product_id.product_name} - Quantity: {self.quantity}"

class MenuProduct(models.Model):
    menu_product_id = models.AutoField(primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_products')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='menu_products')

    def __str__(self) -> str:
        return f"{self.product_id.name} in {self.menu_id.menu_name}"
