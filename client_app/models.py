from django.db import models

# Create your models here.
class CommerceCategory(models.Model):
    commerce_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()