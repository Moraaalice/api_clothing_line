from django.contrib import admin
from product.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
admin.site.register(Product, ProductAdmin)    
