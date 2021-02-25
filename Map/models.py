from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    CATEGORIES = [
        ('Food', 'Food'),
        ('Shelter', 'Shelter'),
        ('Voice', 'Voice'),
        ('Charity Event', 'Charity Event'),
        ('COVID-19', 'COVID-19'),
        ('Litter Picking', 'Litter Picking'),
    ]

    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    name            = models.CharField(null=True, blank=True, max_length=1000)
    latitude        = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=5)
    longitude       = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=5)
    description     = models.TextField(null=True, blank=True)
    category        = models.CharField(max_length=100, choices=CATEGORIES, null=True, blank=True)

class Request(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    place           = models.ForeignKey(Place, on_delete=models.CASCADE)
    description     = models.TextField(null=True, blank=True)