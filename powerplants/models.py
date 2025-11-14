from django.db import models
from ckeditor.fields import RichTextField


class PowerPlant(models.Model):
    PLANT_TYPE_CHOICES = [
        ('TPS', 'Thermal Power Station'),
        ('TPC', 'Thermal Power Central'),
        ('HPP', 'Hydro Power Plant'),
    ]
    
    name = models.CharField(max_length=200)
    plant_type = models.CharField(max_length=3, choices=PLANT_TYPE_CHOICES)
    capacity = models.IntegerField(help_text="Capacity in MW")
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=41.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=69.0)
    description = RichTextField()
    image = models.ImageField(upload_to='powerplants/', blank=True, null=True)
    established_year = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class KeyIndicator(models.Model):
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='indicators/', blank=True, null=True)
    order = models.IntegerField(default=0)
    year = models.IntegerField()
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} - {self.value} {self.unit}"
