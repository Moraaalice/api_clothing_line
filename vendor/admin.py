from django.contrib import admin
from vendor.models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'store_name', 'user_name', 'phone_number']
admin.site.register(Vendor, VendorAdmin)   