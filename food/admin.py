from django.contrib import admin
from .models import FoodItem,Category,Order,OrderItem

# Register your models here.

admin.site.register(FoodItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)


