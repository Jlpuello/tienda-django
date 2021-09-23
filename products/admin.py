from django.contrib import admin
from .models import Products
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields =('title','description','price','image')
    list_display=('__str__','slug','created_at')

admin.site.register(Products, ProductAdmin)