from django.db import models
from customer_app.models import City

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
