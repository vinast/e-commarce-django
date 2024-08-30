from django.contrib import admin
from . models import Product


# ADMIN USERNAME, PASSWORD, EMAIL = root, admin123, root@gmail.com
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']
