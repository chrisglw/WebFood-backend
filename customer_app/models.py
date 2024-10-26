from django.db import models

# Create your models here.
class Customer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to answer', 'I prefer not to answer'),
    ]
    
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    DOB = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=25)

