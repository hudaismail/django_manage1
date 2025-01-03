from django.contrib import admin

from .models import Products, Category
import datetime
from django.utils import timezone

admin.site.register(Category)
admin.site.register(Products)
