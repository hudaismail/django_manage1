from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Products(models.Model):
    name = models.CharField(max_length=150, null=True)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=250, null=True,blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    offer = models.BooleanField(default=False, null=True, blank=False)
    sale_price = models.DecimalField(default=0, decimal_places=2,max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    #digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name
