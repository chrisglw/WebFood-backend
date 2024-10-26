from django.db import models

# Create your models here.
class CommerceCategory(models.Model):
    commerce_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Commerce(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    commerce_id = models.AutoField(primary_key=True)
    commerce_name = models.CharField(max_length=50)
    commerce_description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    commerce_category_id = models.ForeignKey(
        CommerceCategory, on_delete=models.CASCADE, related_name='commerces'
    )

    def __str__(self) -> str:
        return self.commerce_name