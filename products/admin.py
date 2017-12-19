from django.contrib import admin
from .models import Product
from .models import Order
from .models import Profile

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'stock', 'clothingtype', 'gender']
    list_editable = ['name', 'image', 'price', 'stock', 'clothingtype', 'gender']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'adress','ZIP_code']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Profile, ProfileAdmin)
