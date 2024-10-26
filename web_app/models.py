from django.db import models

# Create your models here.
class Landing(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    web_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.name
    
class SectionType(models.Model):
    section_type_id = models.AutoField(primary_key=True)
    section_web = models.CharField(max_length=100) # This might change from CharField to something else
    section_description = models.TextField()

    def __str__(self) -> str:
        return f"{self.section_type_id} - {self.section_description}"